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
        url = reverse('notes_detail', kwargs={'note_id': note["id"]})
        items.append(f"""
            <li>
                <p>                
                    <a href="{url}">
                        {escape(note["title"])}
                    </a>
                    </br>
                    Category: <small>{escape(note["category"])}</small>
                    </br>
                    Tag: <small>{escape(note["tag"])}</small>
                </p>                 
            </li>
""")
    body = f"""
    <h1>Knowledgehub notes list</h1>
    <ul>
        {"".join(items)}
    </ul>
    """
    return HttpResponse(body)


def notes_detail(request: HttpRequest, note_id:int) -> HttpResponse:
    note = data.get_note(note_id)
    body = f"""
        <h1>{escape(note["title"])}</h1>
        <p>
            {escape(note["body"])}
        </p>
        </br>
        Category: <small>{escape(note["category"])}</small>
        </br>
        Tag: <small>{escape(note["tag"])}</small>
        <p>
            <a href="{escape(reverse('notes_list'))}">
                Return to notes list
            </a>
        </p>       
    """

    return HttpResponse(body)