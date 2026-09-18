from copy import deepcopy

from typing import Any

_NOTES: list[dict[str, Any]] = [
    {
        "id": 1,
        "title": "Django introduction",
        "body": "lorem ipsum dolor sit amet",
        "tag": "django",
        "category": "real-life",
    },
    {
        "id": 2,
        "title": "Python basics",
        "body": "Learn the fundamentals of Python programming",
        "tag": "python",
        "category": "programming",
    },
    {
        "id": 3,
        "title": "REST API concepts",
        "body": "Understanding how REST APIs work",
        "tag": "api",
        "category": "backend",
    },
    {
        "id": 4,
        "title": "Database design",
        "body": "Introduction to tables, relationships, and queries",
        "tag": "database",
        "category": "backend",
    },
    {
        "id": 5,
        "title": "Git fundamentals",
        "body": "Learn how to manage code with Git",
        "tag": "git",
        "category": "tools",
    },
    {
        "id": 6,
        "title": "Docker introduction",
        "body": "Learn the basics of containers and Docker",
        "tag": "docker",
        "category": "devops",
    },
    {
        "id": 7,
        "title": "Authentication",
        "body": "Understanding users, passwords, and authentication",
        "tag": "auth",
        "category": "security",
    },
    {
        "id": 8,
        "title": "Testing in Python",
        "body": "Learn how to write and run automated tests",
        "tag": "testing",
        "category": "programming",
    },
    {
        "id": 9,
        "title": "HTML and CSS",
        "body": "Building and styling basic web pages",
        "tag": "frontend",
        "category": "web-development",
    },
    {
        "id": 10,
        "title": "Project deployment",
        "body": "Steps for deploying a web application to production",
        "tag": "deployment",
        "category": "devops",
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
