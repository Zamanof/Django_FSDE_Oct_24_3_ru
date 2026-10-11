from fastapi import FastAPI, Form, Depends
from fastapi.responses import HTMLResponse, FileResponse, Response
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/my-hello")
async def my_hello():
    html = "<h1 style='color:red;'>Hello World</h1>"
    return HTMLResponse(html)

@app.get("/index")
async def index():
    return FileResponse("static/index.html")

@app.get("/index2", response_class=FileResponse)
async def index():
    return "static/index.html"


@app.get("/get-image")
async def get_image():
    return FileResponse("static/fastapi.webp", media_type="image/webp")


@app.get('/download-image')
async def download_image():
    return FileResponse(
        "static/fastapi.webp",
        media_type="application/octet-stream",
        filename="fast.webp",
    )

@app.get('/get-text')
async def get_text():
   html = "<h1 style='color:red;'>Hello World</h1>"
   return Response(html, media_type="text/plain")


class User(BaseModel):
    email: str
    password: str


def as_user_from_form(
        email: str=Form(...),
        password: str=Form(...),
)->User:
    return User(email=email, password=password)


@app.post("/login")
async def login(user: User = Depends(as_user_from_form)):
    return {'message': f'Email: "{user.email}" Password: "{user.password}"'}


@app.post("/my_login")
async def my_login(user: User):
    return {'message': f'Email: "{user.email}" Password: "{user.password}"'}


