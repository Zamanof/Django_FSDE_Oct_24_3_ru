from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import escape

from notes import data


# ============================================================
# ОБЩИЙ HTML ШАБЛОН
# ============================================================

def html_shell(title: str, body: str) -> str:
    safe_title = escape(title)

    return f"""
<!DOCTYPE html>
<html lang="ru">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>{safe_title}</title>

    <style>

        /* ==================================================
           BASE
           ================================================== */

        * {{
            box-sizing: border-box;
        }}


        ::selection {{
            background: #111;
            color: #d8ff00;
        }}


        body {{
            margin: 0;
            min-height: 100vh;

            padding: 70px 8vw 100px;

            background:
                linear-gradient(
                    rgba(0, 0, 0, 0.035) 1px,
                    transparent 1px
                ),
                linear-gradient(
                    90deg,
                    rgba(0, 0, 0, 0.035) 1px,
                    transparent 1px
                ),
                #f2f0e9;

            background-size: 24px 24px;

            color: #111;

            font-family:
                "Courier New",
                Courier,
                monospace;
        }}


        /* ==================================================
           ГЛАВНЫЙ ЗАГОЛОВОК
           ================================================== */

        h1 {{
            max-width: 950px;

            margin: 0 auto 45px;

            padding: 0 0 18px;

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            font-size: clamp(42px, 7vw, 85px);

            font-weight: 900;

            line-height: 0.9;

            letter-spacing: -4px;

            text-transform: uppercase;

            border-bottom: 8px solid #111;

            overflow-wrap: anywhere;
        }}


        h1::before {{
            content: "KNOWLEDGE / HUB";

            display: block;

            margin-bottom: 18px;

            font-family:
                "Courier New",
                monospace;

            font-size: 12px;

            font-weight: normal;

            letter-spacing: 4px;

            color: #555;
        }}


        /* ==================================================
           ОБЫЧНЫЙ ТЕКСТ
           ================================================== */

        body > p {{
            max-width: 950px;

            margin: 25px auto;

            font-size: 17px;

            line-height: 1.7;
        }}


        p {{
            line-height: 1.6;
        }}


        strong {{
            font-weight: 900;
        }}


        /* ==================================================
           ССЫЛКИ
           ================================================== */

        a {{
            color: #111;

            text-decoration: none;

            font-weight: 700;
        }}


        /* ==================================================
           СПИСОК ЗАМЕТОК
           ================================================== */

        ul {{
            max-width: 950px;

            margin: 50px auto 0;

            padding: 0;

            list-style: none;

            border-top: 5px solid #111;
        }}


        li {{
            position: relative;

            margin: 0;

            padding:
                28px
                25px
                28px
                70px;

            border-bottom: 2px solid #111;

            transition:
                padding-left 0.15s ease,
                background 0.15s ease;
        }}


        li::before {{
            content: "↳";

            position: absolute;

            left: 15px;

            top: 23px;

            font-size: 30px;

            font-weight: bold;
        }}


        li:hover {{
            padding-left: 85px;

            background: #d8ff00;
        }}


        /* ==================================================
           НАЗВАНИЕ ЗАМЕТКИ
           ================================================== */

        .note-title {{
            display: inline-block;

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            font-size:
                clamp(24px, 4vw, 40px);

            font-weight: 900;

            letter-spacing: -1.5px;

            line-height: 1.05;

            text-transform: uppercase;

            overflow-wrap: anywhere;

            transition: 0.15s;
        }}


        .note-title:hover {{
            background: #111;

            color: #d8ff00;

            padding: 3px 7px;
        }}


        /* ==================================================
           CATEGORY / TAG
           ================================================== */

        .note-meta {{
            max-width: 950px;

            margin: 25px auto;

            font-size: 13px;

            line-height: 2;

            letter-spacing: 1px;

            text-transform: uppercase;
        }}


        li .note-meta {{
            margin:
                15px
                0
                0;
        }}


        small {{
            display: inline-block;

            margin:
                4px
                10px
                4px
                3px;

            padding: 4px 8px;

            background: #111;

            color: #f2f0e9;

            font-size: 11px;

            letter-spacing: 1px;

            text-transform: uppercase;
        }}


        /* ==================================================
           DETAIL PAGE
           ================================================== */

        .note-content {{
            max-width: 950px;

            margin: 0 auto 30px;

            font-family:
                Georgia,
                "Times New Roman",
                serif;

            font-size: 21px;

            line-height: 1.8;

            white-space: pre-wrap;

            overflow-wrap: anywhere;
        }}


        /* ==================================================
           ACTIONS
           ================================================== */

        .actions {{
            max-width: 950px;

            margin: 35px auto 0;

            display: flex;

            flex-wrap: wrap;

            gap: 15px;

            align-items: center;
        }}


        .action-link {{
            display: inline-block;

            padding: 14px 20px;

            border: 3px solid #111;

            background: transparent;

            color: #111;

            font-family:
                "Courier New",
                Courier,
                monospace;

            font-size: 13px;

            font-weight: 700;

            letter-spacing: 1px;

            text-transform: uppercase;

            box-shadow: 6px 6px 0 #111;

            transition: 0.15s;
        }}


        .action-link:hover {{
            background: #d8ff00;

            color: #111;

            transform: translate(3px, 3px);

            box-shadow: 3px 3px 0 #111;
        }}


        .action-link:active {{
            transform: translate(6px, 6px);

            box-shadow: none;
        }}


        /* ==================================================
           КНОПКА УДАЛИТЬ
           ================================================== */

        .danger-link {{
            background: #111;

            color: #f2f0e9;
        }}


        .danger-link:hover {{
            background: #d8ff00;

            color: #111;
        }}


        /* ==================================================
           FORM
           ================================================== */

        form {{
            max-width: 950px;

            margin: 0 auto;

            padding: 0;

            font-family:
                "Courier New",
                Courier,
                monospace;
        }}


        form h1 {{
            margin-bottom: 50px;
        }}


        form p {{
            margin: 0 0 20px;
        }}


        /* ==================================================
           LABEL
           ================================================== */

        form label {{
            display: inline-block;

            margin-bottom: 4px;

            font-size: 12px;

            font-weight: 700;

            letter-spacing: 2px;

            text-transform: uppercase;
        }}


        form label::before {{
            content: "→ ";

            color: #111;
        }}


        /* ==================================================
           INPUT
           ================================================== */

        form input[type="text"] {{
            width: 100%;

            padding: 17px 18px;

            background: transparent;

            color: #111;

            border: 0;

            border-bottom: 3px solid #111;

            outline: none;

            font-family:
                "Courier New",
                Courier,
                monospace;

            font-size: 19px;

            transition: 0.15s;
        }}


        form input[type="text"]:focus {{
            background: #d8ff00;

            border-bottom-width: 6px;

            padding-left: 25px;
        }}


        form input::placeholder {{
            color: #777;
        }}


        form input:required {{
            border-left: 5px solid #111;
        }}


        form input:required:valid {{
            border-left-color: #d8ff00;
        }}


        /* ==================================================
           TEXTAREA
           ================================================== */

        form textarea {{
            width: 100%;

            min-height: 220px;

            padding: 18px;

            background: transparent;

            color: #111;

            border: 3px solid #111;

            outline: none;

            font-family:
                "Courier New",
                Courier,
                monospace;

            font-size: 17px;

            line-height: 1.6;

            resize: vertical;

            transition: 0.15s;
        }}


        form textarea:focus {{
            background: #d8ff00;

            border-width: 5px;

            padding-left: 24px;
        }}


        form textarea::placeholder {{
            color: #777;
        }}


        /* ==================================================
           BUTTON
           ================================================== */

        form button {{
            margin-top: 20px;

            padding: 17px 32px;

            background: #111;

            color: #d8ff00;

            border: 3px solid #111;

            font-family:
                "Courier New",
                Courier,
                monospace;

            font-size: 15px;

            font-weight: 700;

            letter-spacing: 2px;

            text-transform: uppercase;

            cursor: pointer;

            box-shadow: 7px 7px 0 #d8ff00;

            transition: 0.15s;
        }}


        form button::after {{
            content: " →";
        }}


        form button:hover {{
            background: #d8ff00;

            color: #111;

            box-shadow: 7px 7px 0 #111;

            transform: translate(-2px, -2px);
        }}


        form button:active {{
            transform: translate(5px, 5px);

            box-shadow: 2px 2px 0 #111;
        }}


        /* ==================================================
           ERROR
           ================================================== */

        .form-error {{
            margin-bottom: 30px;

            padding: 15px 20px;

            background: #111;

            color: #d8ff00;

            border-left: 10px solid #d8ff00;

            font-size: 14px;

            font-weight: 700;

            text-transform: uppercase;

            box-shadow: 6px 6px 0 #d8ff00;
        }}


        /* ==================================================
           DELETE WARNING
           ================================================== */

        .delete-warning {{
            max-width: 950px;

            margin: 0 auto 35px;

            padding: 25px;

            border: 4px solid #111;

            box-shadow: 8px 8px 0 #111;
        }}


        .delete-warning-label {{
            display: inline-block;

            margin-bottom: 15px;

            padding: 5px 10px;

            background: #111;

            color: #d8ff00;

            font-size: 12px;

            font-weight: 700;

            letter-spacing: 2px;

            text-transform: uppercase;
        }}


        .delete-warning p {{
            margin: 8px 0;

            font-family:
                "Courier New",
                Courier,
                monospace;

            font-size: 16px;

            line-height: 1.6;
        }}


        /* ==================================================
           EMPTY
           ================================================== */

        .empty-message {{
            max-width: 950px;

            margin: 30px auto;

            padding: 25px;

            border:
                3px
                dashed
                #111;

            font-size: 16px;

            font-weight: bold;

            text-transform: uppercase;
        }}


        /* ==================================================
           MOBILE
           ================================================== */

        @media (max-width: 600px) {{

            body {{
                padding:
                    40px
                    20px
                    70px;
            }}


            h1 {{
                font-size: 44px;

                letter-spacing: -2px;
            }}


            li {{
                padding-left: 50px;
            }}


            li:hover {{
                padding-left: 55px;
            }}


            li::before {{
                left: 8px;
            }}


            .actions {{
                flex-direction: column;

                align-items: stretch;
            }}


            .action-link {{
                text-align: center;
            }}

        }}

    </style>

</head>


<body>

    {body}

</body>

</html>
"""


# ============================================================
# CSRF
# ============================================================

def _csrf_field(request: HttpRequest) -> str:
    token = get_token(request)

    return (
        f"<input "
        f"type='hidden' "
        f"name='csrfmiddlewaretoken' "
        f"value='{escape(token)}'"
        f">"
    )


# ============================================================
# ГЛАВНАЯ
# ============================================================

def index(request: HttpRequest) -> HttpResponse:

    notes_url = escape(
        reverse("notes_list")
    )

    create_url = escape(
        reverse("notes_create")
    )

    body = f"""

        <h1>
            Добро пожаловать в Knowledge Hub
        </h1>


        <p>
            Здесь вы можете создавать,
            просматривать, редактировать
            и удалять свои заметки.
        </p>


        <div class="actions">

            <a
                class="action-link"
                href="{notes_url}"
            >
                Список заметок
            </a>


            <a
                class="action-link"
                href="{create_url}"
            >
                Создать заметку
            </a>

        </div>

    """

    return HttpResponse(
        html_shell(
            "Главная — Knowledge Hub",
            body
        )
    )


# ============================================================
# О ПРОЕКТЕ
# ============================================================

def about(request: HttpRequest) -> HttpResponse:

    body = """

        <h1>
            О проекте Knowledge Hub
        </h1>


        <p>
            Knowledge Hub — учебный проект
            для создания, хранения,
            просмотра и управления заметками.
        </p>

    """

    return HttpResponse(
        html_shell(
            "О проекте — Knowledge Hub",
            body
        )
    )


# ============================================================
# СПИСОК ЗАМЕТОК
# ============================================================

def notes_list(
        request: HttpRequest
) -> HttpResponse:

    raw_tag = request.GET.get("tag")

    raw_category = request.GET.get(
        "category"
    )


    notes = data.list_notes()


    # --------------------------------------------------------
    # ФИЛЬТР ПО ТЕГУ
    # --------------------------------------------------------

    if raw_tag:

        tag_filter = (
            raw_tag
            .strip()
            .lower()
        )

        notes = [
            note
            for note in notes
            if note["tag"].lower()
            == tag_filter
        ]


    # --------------------------------------------------------
    # ФИЛЬТР ПО КАТЕГОРИИ
    # --------------------------------------------------------

    if raw_category:

        category_filter = (
            raw_category
            .strip()
            .lower()
        )

        notes = [
            note
            for note in notes
            if note["category"].lower()
            == category_filter
        ]


    # --------------------------------------------------------
    # СОЗДАЁМ HTML ЗАМЕТОК
    # --------------------------------------------------------

    items: list[str] = []


    for note in notes:

        url = escape(
            reverse(
                "notes_detail",
                kwargs={
                    "note_id": note["id"]
                }
            )
        )


        items.append(
            f"""

            <li>

                <a
                    class="note-title"
                    href="{url}"
                >
                    {escape(note["title"])}
                </a>


                <div class="note-meta">

                    Категория:

                    <small>
                        {escape(note["category"])}
                    </small>


                    Тег:

                    <small>
                        {escape(note["tag"])}
                    </small>

                </div>

            </li>

            """
        )


    # --------------------------------------------------------
    # ЕСЛИ ЗАМЕТОК НЕТ
    # --------------------------------------------------------

    if items:

        notes_html = f"""
            <ul>
                {"".join(items)}
            </ul>
        """

    else:

        notes_html = """

            <div class="empty-message">
                Заметки не найдены.
            </div>

        """


    create_url = escape(
        reverse("notes_create")
    )


    body = f"""

        <h1>
            Заметки Knowledge Hub
        </h1>


        <div class="actions">

            <a
                class="action-link"
                href="{create_url}"
            >
                + Новая заметка
            </a>

        </div>


        {notes_html}

    """


    return HttpResponse(
        html_shell(
            "Список заметок — Knowledge Hub",
            body
        )
    )


# ============================================================
# ДЕТАЛЬНАЯ СТРАНИЦА ЗАМЕТКИ
# ============================================================

def notes_detail(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:

    note = data.get_note(note_id)


    # --------------------------------------------------------
    # ЗАМЕТКА НЕ НАЙДЕНА
    # --------------------------------------------------------

    if note is None:

        list_url = escape(
            reverse("notes_list")
        )

        body = f"""

            <h1>
                Заметка не найдена
            </h1>


            <p>
                Запрошенная заметка
                не существует.
            </p>


            <div class="actions">

                <a
                    class="action-link"
                    href="{list_url}"
                >
                    ← Вернуться к заметкам
                </a>

            </div>

        """

        return HttpResponse(
            html_shell(
                "Заметка не найдена",
                body
            ),
            status=404
        )


    # --------------------------------------------------------
    # URL
    # --------------------------------------------------------

    list_url = escape(
        reverse("notes_list")
    )


    update_url = escape(
        reverse(
            "notes_update",
            kwargs={
                "note_id": note_id
            }
        )
    )


    delete_url = escape(
        reverse(
            "notes_delete",
            kwargs={
                "note_id": note_id
            }
        )
    )


    # --------------------------------------------------------
    # HTML
    # --------------------------------------------------------

    body = f"""

        <h1>
            {escape(note["title"])}
        </h1>


        <div class="note-content">
{escape(note["body"])}
        </div>


        <div class="note-meta">

            Категория:

            <small>
                {escape(note["category"])}
            </small>


            Тег:

            <small>
                {escape(note["tag"])}
            </small>

        </div>


        <div class="actions">


            <a
                class="action-link"
                href="{list_url}"
            >
                ← К списку
            </a>


            <a
                class="action-link"
                href="{update_url}"
            >
                ✎ Изменить
            </a>


            <a
                class="action-link danger-link"
                href="{delete_url}"
            >
                × Удалить
            </a>


        </div>

    """


    return HttpResponse(
        html_shell(
            f"{note['title']} — Knowledge Hub",
            body
        )
    )


# ============================================================
# СОЗДАНИЕ ЗАМЕТКИ
# ============================================================

def notes_create(
        request: HttpRequest
) -> HttpResponse:

    error = ""


    # --------------------------------------------------------
    # POST
    # --------------------------------------------------------

    if request.method == "POST":

        title = request.POST.get(
            "title",
            ""
        )

        note_body = request.POST.get(
            "body",
            ""
        )

        tag = request.POST.get(
            "tag",
            ""
        )

        category = request.POST.get(
            "category",
            ""
        )


        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not title.strip():

            error = """

                <div class="form-error">
                    Заголовок не может
                    быть пустым.
                </div>

            """


        else:

            created = data.create_note(

                title=title,

                body=note_body,

                tag=(
                    tag
                    or "смешанная"
                ),

                category=(
                    category
                    or "главная"
                ),
            )


            # После создания сразу
            # переходим на страницу заметки.

            return redirect(
                "notes_detail",
                note_id=created["id"]
            )


    # --------------------------------------------------------
    # FORM
    # --------------------------------------------------------

    action = escape(
        reverse("notes_create")
    )


    list_url = escape(
        reverse("notes_list")
    )


    form = f"""

        <form
            method="post"
            action="{action}"
        >


            {error}


            {_csrf_field(request)}


            <h1>
                Новая заметка
            </h1>


            <p>
                <label>
                    Заголовок
                </label>
            </p>


            <p>

                <input
                    type="text"
                    name="title"
                    placeholder="Введите заголовок"
                    required
                >

            </p>


            <p>
                <label>
                    Текст заметки
                </label>
            </p>


            <p>

                <textarea
                    name="body"
                    placeholder="Введите текст заметки"
                    required
                ></textarea>

            </p>


            <p>
                <label>
                    Категория
                </label>
            </p>


            <p>

                <input
                    type="text"
                    name="category"
                    placeholder="Например: Backend"
                    required
                >

            </p>


            <p>
                <label>
                    Тег
                </label>
            </p>


            <p>

                <input
                    type="text"
                    name="tag"
                    placeholder="Например: Django"
                    required
                >

            </p>


            <p>

                <button type="submit">
                    Создать
                </button>

            </p>


            <div class="actions">

                <a
                    class="action-link"
                    href="{list_url}"
                >
                    Отмена
                </a>

            </div>


        </form>

    """


    return HttpResponse(
        html_shell(
            "Новая заметка — Knowledge Hub",
            form
        )
    )


# ============================================================
# РЕДАКТИРОВАНИЕ ЗАМЕТКИ
# ============================================================

def notes_update(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:

    note = data.get_note(note_id)


    # --------------------------------------------------------
    # ЗАМЕТКА НЕ НАЙДЕНА
    # --------------------------------------------------------

    if note is None:

        list_url = escape(
            reverse("notes_list")
        )

        body = f"""

            <h1>
                Редактирование невозможно
            </h1>


            <p>
                Запрошенная заметка
                не найдена.
            </p>


            <div class="actions">

                <a
                    class="action-link"
                    href="{list_url}"
                >
                    Вернуться к списку
                </a>

            </div>

        """

        return HttpResponse(
            html_shell(
                "Заметка не найдена",
                body
            ),
            status=404
        )


    error = ""


    # --------------------------------------------------------
    # POST
    # --------------------------------------------------------

    if request.method == "POST":

        title = request.POST.get(
            "title",
            ""
        )

        note_body = request.POST.get(
            "body",
            ""
        )

        tag = request.POST.get(
            "tag",
            ""
        )

        category = request.POST.get(
            "category",
            ""
        )


        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not title.strip():

            error = """

                <div class="form-error">
                    Заголовок не может
                    быть пустым.
                </div>

            """


            # Сохраняем введённые пользователем
            # данные для повторного отображения.

            note = {
                **note,

                "title": title,

                "body": note_body,

                "tag": tag,

                "category": category,
            }


        else:

            data.update_note(

                note_id,

                title=title,

                body=note_body,

                tag=(
                    tag
                    or "смешанная"
                ),

                category=(
                    category
                    or "главная"
                ),
            )


            return redirect(
                "notes_detail",
                note_id=note_id
            )


    # --------------------------------------------------------
    # ESCAPE
    # --------------------------------------------------------

    title_e = escape(
        note["title"]
    )

    body_e = escape(
        note["body"]
    )

    tag_e = escape(
        note["tag"]
    )

    category_e = escape(
        note["category"]
    )


    # --------------------------------------------------------
    # URL
    # --------------------------------------------------------

    action = escape(

        reverse(

            "notes_update",

            kwargs={
                "note_id": note_id
            }

        )
    )


    cancel_url = escape(

        reverse(

            "notes_detail",

            kwargs={
                "note_id": note_id
            }

        )
    )


    # --------------------------------------------------------
    # FORM
    # --------------------------------------------------------

    form = f"""

        <form
            method="post"
            action="{action}"
        >


            {error}


            {_csrf_field(request)}


            <h1>
                Редактирование заметки
            </h1>


            <p>
                <label>
                    Заголовок
                </label>
            </p>


            <p>

                <input
                    type="text"
                    name="title"
                    required
                    value="{title_e}"
                >

            </p>


            <p>
                <label>
                    Текст заметки
                </label>
            </p>


            <p>

                <textarea
                    name="body"
                    required
                >{body_e}</textarea>

            </p>


            <p>
                <label>
                    Категория
                </label>
            </p>


            <p>

                <input
                    type="text"
                    name="category"
                    required
                    value="{category_e}"
                >

            </p>


            <p>
                <label>
                    Тег
                </label>
            </p>


            <p>

                <input
                    type="text"
                    name="tag"
                    required
                    value="{tag_e}"
                >

            </p>


            <p>

                <button type="submit">
                    Сохранить изменения
                </button>

            </p>


            <div class="actions">

                <a
                    class="action-link"
                    href="{cancel_url}"
                >
                    Отмена
                </a>

            </div>


        </form>

    """


    return HttpResponse(
        html_shell(
            "Редактирование заметки — Knowledge Hub",
            form
        )
    )


# ============================================================
# УДАЛЕНИЕ ЗАМЕТКИ
# ============================================================

def notes_delete(
        request: HttpRequest,
        note_id: int
) -> HttpResponse:

    note = data.get_note(note_id)


    # --------------------------------------------------------
    # ЗАМЕТКА НЕ НАЙДЕНА
    # --------------------------------------------------------

    if note is None:

        list_url = escape(
            reverse("notes_list")
        )

        body = f"""

            <h1>
                Удаление невозможно
            </h1>


            <p>
                Запрошенная заметка
                не найдена.
            </p>


            <div class="actions">

                <a
                    class="action-link"
                    href="{list_url}"
                >
                    Вернуться к списку
                </a>

            </div>

        """

        return HttpResponse(
            html_shell(
                "Заметка не найдена",
                body
            ),
            status=404
        )


    # --------------------------------------------------------
    # POST — УДАЛЯЕМ
    # --------------------------------------------------------

    if request.method == "POST":

        data.delete_note(note_id)

        return redirect(
            "notes_list"
        )


    # --------------------------------------------------------
    # URL
    # --------------------------------------------------------

    action = escape(

        reverse(

            "notes_delete",

            kwargs={
                "note_id": note_id
            }

        )
    )


    cancel_url = escape(

        reverse(

            "notes_detail",

            kwargs={
                "note_id": note_id
            }

        )
    )


    # --------------------------------------------------------
    # HTML
    # --------------------------------------------------------

    body = f"""

        <h1>
            Удаление заметки
        </h1>


        <div class="delete-warning">


            <span class="delete-warning-label">
                Внимание
            </span>


            <p>

                Вы действительно хотите
                удалить заметку

                <strong>
                    {escape(note["title"])}
                </strong>?

            </p>


            <p>
                Это действие нельзя отменить.
            </p>


        </div>


        <form
            method="post"
            action="{action}"
        >


            {_csrf_field(request)}


            <button type="submit">
                Да, удалить
            </button>


        </form>


        <div class="actions">

            <a
                class="action-link"
                href="{cancel_url}"
            >
                Отмена
            </a>

        </div>

    """


    return HttpResponse(
        html_shell(
            "Удаление заметки — Knowledge Hub",
            body
        )
    )