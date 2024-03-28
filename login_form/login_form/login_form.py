import reflex as rx
from login_form.pages import *  # noqa: F403
from login_form.api.api import hello


app = rx.App()

app.api.add_api_route("/hello", hello)
