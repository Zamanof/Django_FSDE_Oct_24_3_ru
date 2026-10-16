from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from notes.models import Note, Category
from notes.forms import NoteForm

# Arrange
# Act
# Assert

class NotesFormTest(SimpleTestCase):
    def test_valid_data_passes_validation(self):
        # Arrange
        form = NoteForm(
            data={
                'title': 'First note title',
                'content': 'First note content',
            }
        )
        # Act       - form.is_valid()
        # Assert    - self.assertTrue()

        self.assertTrue(form.is_valid())

    def test_empty_title_is_rejected(self):
        form = NoteForm(
            data={
                'title': '',
                'content': 'First note content',
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class NoteCreateAccessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            username='John',
            password='P@ss123456')
        cls.create_url = reverse('notes:notes_create')
        cls.login_url = reverse('accounts:login')

    def test_guest_is_redirected_to_login(self):
        response = self.client.get(self.create_url)

        self.assertRedirects(response, f'{self.login_url}?next={self.create_url}')

    def test_authenticated_user_can_open_create_form(self):
        self.client.force_login(self.author)

        response = self.client.get(self.create_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_create.html')
        self.assertContains(response, 'Заголовок')

class NoteCreatePostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            username='John',
            password='P@ss123456')

    def setUp(self):
        self.client.force_login(self.author)

    def test_post_create_note_for_current_user(self):
        before = Note.objects.count()

        response = self.client.post(
            reverse('notes:notes_create'),
            data={
                'title': 'First note title',
                'content': 'First note content',
            }
        )

        self.assertEqual(Note.objects.count(), before + 1)
        note = Note.objects.get(title='First note title')
        self.assertEqual(note.content, 'First note content')
        self.assertEqual(note.author, self.author)
        self.assertRedirects(
            response,
            reverse('notes:notes_detail', args=[note.pk]))

class NoteOwnershipTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            username='John',
            password='P@ss123456')

        cls.intruder = User.objects.create_user(
            username='Doe',
            password='P@ss123456'
        )

        cls.note = Note.objects.create(
            title='First note title',
            content='First note content',
            author=cls.author,
        )

    def test_author_can_edit_note(self):
        self.client.force_login(self.author)

        response = self.client.post(reverse(
            'notes:notes_update',
            args=[self.note.id]),
        {
            'title': 'New title',
            'content': 'First note content',
        })

        self.assertRedirects(
            response,
        reverse('notes:notes_detail', args=[self.note.id]))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'New title')

    def test_other_user_cannot_edit_note(self):
        original_title = self.note.title
        original_content = self.note.content
        self.client.force_login(self.intruder)

        response = self.client.post(reverse(
            'notes:notes_update',
            args=[self.note.id]),
        {
            'title': 'New title',
            'content': 'First note content',
        })

        self.assertEqual(response.status_code, 403)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, original_title)
        self.assertEqual(self.note.content, original_content)

