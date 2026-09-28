from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from notes import data
from notes.forms import ContactForm, NoteForm


def index(request: HttpRequest):
    return render(request, 'notes/home.html')

def about(request: HttpRequest):
    return render(request, 'notes/about.html')

def contact(request: HttpRequest):
    form = ContactForm()
    return render(request, 'notes/contact.html', {'form': form})

def notes_list(
        request: HttpRequest
) -> HttpResponse:
    notes = data.list_notes()
    return render(request, 'notes/notes_list.html', {'notes': notes})


def notes_detail(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:
    note = data.get_note(note_id)
    return render(request, 'notes/note_detail.html', {'note': note})


def notes_create(
        request: HttpRequest
) -> HttpResponse:
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            notes = request.session.get('notes', [])
            notes.append({
                'title': form.cleaned_data['title'],
                'content': form.cleaned_data['content'],
                'category': form.cleaned_data['category'],
                'tags': form.cleaned_data['tags'],
            })
            request.session['notes'] = notes
            data.create_note(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                category=form.cleaned_data['category'],
                tags=form.cleaned_data['tags'].split()
            )
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {'form': form})
def notes_update(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:
    note = data.get_note(note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags'].split()
            data.update_note(
                note_id,
                title=title,
                content=content,
                category=category,
                tags=tags
            )
            return redirect('notes_list')
    else:
        form = NoteForm(initial=note)
    return render(request, 'notes/note_create.html', {'form': form})

def notes_delete(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:
   pass