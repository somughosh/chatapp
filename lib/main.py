from typing import Annotated

from fastapi import FastAPI, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from . import db


app = FastAPI()
app.mount("/ui", StaticFiles(directory="ui"), name="ui")


@app.get("/")
def get_root():
    return "Root"


@app.post("/login")
def post_login(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    if db.get_user(email) == db.DEFAULT_USER:
        db.set_user(email=email, password=password)
        return RedirectResponse("/ui/html/chat.html", status_code=status.HTTP_302_FOUND)

    elif db.get_check_valid_password(email, password):
        return RedirectResponse("/ui/html/chat.html", status_code=status.HTTP_302_FOUND)
    else:
        return RedirectResponse(
            "/ui/html/login.html?status=failed", status_code=status.HTTP_302_FOUND
        )


@app.get("/login")
def get_login():
    return "GET LOGIN"
