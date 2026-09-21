from copy import deepcopy
from datetime import datetime
from typing import Any


_NOTES: list[dict[str, Any]] = [
    {
        "id": 1,
        "title": "Django introduction",
        "content": "Lorem ipsum dolor sit amet",
        "tags": ["python", "django"],
        "category": "backend",
        "created_at": datetime(2026, 9, 21),
    },
    {
        "id": 2,
        "title": "Python basics",
        "content": "Learn the fundamentals of Python programming",
        "tags": ["python", "basics", "programming"],
        "category": "programming",
        "created_at": datetime(2026, 9, 18),
    },
    {
        "id": 3,
        "title": "REST API concepts",
        "content": "Understanding how REST APIs work",
        "tags": ["api", "rest", "http", "backend"],
        "category": "backend",
        "created_at": datetime(2026, 9, 15),
    },
    {
        "id": 4,
        "title": "Database design",
        "content": "Introduction to tables, relationships, and queries",
        "tags": ["database", "sql", "tables", "relationships", "backend"],
        "category": "backend",
        "created_at": datetime(2026, 9, 11),
    },
    {
        "id": 5,
        "title": "Git fundamentals",
        "content": "Learn how to manage code with Git",
        "tags": ["git", "github", "version-control"],
        "category": "tools",
        "created_at": datetime(2026, 9, 7),
    },
    {
        "id": 6,
        "title": "Docker introduction",
        "content": "Learn the basics of containers and Docker",
        "tags": ["docker", "containers", "devops", "deployment"],
        "category": "devops",
        "created_at": datetime(2026, 8, 30),
    },
    {
        "id": 7,
        "title": "Authentication",
        "content": "Understanding users, passwords, and authentication",
        "tags": [
            "auth",
            "security",
            "password",
            "jwt",
            "users",
            "backend",
        ],
        "category": "security",
        "created_at": datetime(2026, 8, 25),
    },
    {
        "id": 8,
        "title": "Testing in Python",
        "content": "Learn how to write and run automated tests",
        "tags": ["python", "testing", "pytest", "automation"],
        "category": "programming",
        "created_at": datetime(2026, 8, 19),
    },
    {
        "id": 9,
        "title": "HTML and CSS",
        "content": "Building and styling basic web pages",
        "tags": ["html", "css", "frontend", "web", "design"],
        "category": "web-development",
        "created_at": datetime(2026, 8, 12),
    },
    {
        "id": 10,
        "title": "Project deployment",
        "content": "Steps for deploying a web application to production",
        "tags": ["deployment", "devops", "server", "linux"],
        "category": "devops",
        "created_at": datetime(2026, 8, 3),
    },
]

_next_id = 11

def list_notes() -> list[dict[str, Any]]:
    return deepcopy(_NOTES)

def get_note(note_id: int) -> dict[str, Any]|None:
    for note in _NOTES:
        if note["id"] == note_id:
            return deepcopy(note)
    return None


def create_note(
        *,
        title:str,
        body:str,
        tag:str,
        category:str,
) -> dict[str, Any]:
    global _next_id
    note = {
        "id": _next_id,
        "title": title.strip(),
        "body": body.strip(),
        "tag": tag.strip(),
        "category": category.strip(),
    }
    _NOTES.append(note)
    _next_id += 1
    return deepcopy(note)


def update_note(
        note_id: int,
        *,
        title:str,
        body:str,
        tag:str,
        category:str,
)->dict[str, Any] | None:
    for note in _NOTES:
        if note["id"] == note_id:
            note["title"] = title.strip()
            note["body"] = body.strip()
            note["tag"] = tag.strip()
            note["category"] = category.strip()
            return deepcopy(note)
        return None
    return None


def delete_note(note_id: int) -> bool:
    global _NOTES
    before = len(_NOTES)
    _NOTES = [n for n in _NOTES if n['id'] != note_id]
    return before != len(_NOTES)