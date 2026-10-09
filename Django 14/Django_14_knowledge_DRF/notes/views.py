from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404

from notes.forms import NoteForm, ContactForm
from notes.models import Note

from django.contrib.auth.decorators import login_required



def index(request: HttpRequest):
    return render(request, 'notes/home.html')

def about(request: HttpRequest):
    return render(request, 'notes/about.html')

def contact(request: HttpRequest):
    form = ContactForm()
    return render(request, 'notes/contact.html', {'form': form})

@login_required
def notes_list(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.filter(author=request.user).order_by('-created_at')

    return render(request, 'notes/notes_list.html', {'notes': notes})


@login_required
def notes_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(
        Note.objects.select_related('author', 'category').prefetch_related('tags'),
        pk=note_id
    )
    if note.author != request.user:
        return HttpResponseForbidden(
            "Вы можете просматривать только свои заметки."
        )

    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
def notes_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            messages.success(request, 'Заметка успешно создана')
            return redirect('notes:notes_detail', note_id=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {'form': form})


@login_required
def notes_update(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)
    if note.author != request.user:
        return HttpResponseForbidden(
            "Вы можете редактировать только свои заметки."
        )
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заметка успешно обновлена')
            return redirect('notes:notes_detail', note_id=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form, 'note': note})


@login_required
def notes_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)
    if note.author != request.user:
        return HttpResponseForbidden(
            "Вы можете удалять только свои заметки."
        )
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Заметка успешно удалена')
        return redirect('notes:notes_list')
    return render(request, 'notes/note_delete.html', {'note': note})
