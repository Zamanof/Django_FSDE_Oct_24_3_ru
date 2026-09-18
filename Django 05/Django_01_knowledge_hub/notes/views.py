from django.http import HttpRequest, HttpResponse

from django.urls import reverse
from django.utils.html import escape

from notes import data


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    body =f"""
    <h1>Добро пожаловать!!! Это главная страница!!!</h1>
    <p>
        <a href="{escape(reverse('notes_list'))}">
        Перейдите на списку заметок
        </a>
    </p>
    """

    return HttpResponse(body)


def about(request: HttpRequest) -> HttpResponse:
    body =f"""
    <h1>О проекте Knowledge Hub</h1>
    <p>
        Это безумно крутой проект!!!
    </p>
    """

    return HttpResponse(body)


def notes_list(request: HttpRequest) -> HttpResponse:
    notes = data.list_notes()
    items: list[str] = []
    for note in notes:
        items.append(f"""
            <li>{escape(note["title"])}</li>
""")
    return HttpResponse(items)