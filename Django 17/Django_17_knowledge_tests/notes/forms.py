from django import forms

from notes.models import Note


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        min_length=1,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={'placeholder': 'Введите вашу почту'}),
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'placeholder': 'Введите сообщение', 'rows': '5'}),
    )


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'tags']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'category': 'Категория',
            'tags': 'Теги',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Введите содержание заметки',
            }),
            'category': forms.Select(),
            'tags': forms.SelectMultiple(),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if title.lower().startswith('test'):
            raise forms.ValidationError('Заголовок не должен начинаться с «test»')
        return title
