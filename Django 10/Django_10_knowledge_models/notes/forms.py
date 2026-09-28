from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        min_length=1,
        widget=forms.TextInput(attrs={'placeholder':'Enter your name'})
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={'placeholder':'Enter your message', 'rows':'5'}),
    )


class NoteForm(forms.Form):
    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('work', 'Work'),
        ('backend', "Backend"),
        ('frontend', 'Frontend'),
    ]
    title = forms.CharField(
        label="Title",
        min_length=5,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Enter your title'})
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={'placeholder':'Enter your content', 'rows':'6'}, ),
        min_length=5,
    )
    tags = forms.CharField(
        label="Tags",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder':'Enter your tags. Example: django python'})
    )
    category = forms.ChoiceField(
        label="Category",
        choices=CATEGORY_CHOICES,
    )

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if title.lower().startswith('test'):
            raise forms.ValidationError("Title should not start with 'test'")
        return title

