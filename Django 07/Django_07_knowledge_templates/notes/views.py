from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import escape

from notes import data



def index(request: HttpRequest):
    return render(request, 'notes/home.html')




def about(request: HttpRequest):
    return render(request, 'notes/about.html')

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
    pass

def notes_update(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:

   pass

def notes_delete(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:
   pass