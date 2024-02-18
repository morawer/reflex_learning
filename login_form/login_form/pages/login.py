import reflex as rx
from login_form.styles import auth_pages_stylesheet
from login_form.components.input_field import render_input_field
from login_form.components.button import render_submit_button
from login_form.states import LoginState


@rx.page(route="/")
def login():
    return rx.vstack(
        rx.hstack(
            rx.icon("sun-moon"),
            width="100%",
            justify_content="end",
        ),
        rx.spacer(),
        rx.heading(
            "Welcome Back!", size="9",
            transition="all 550ms ease"
        ),
        rx.text("Sign in bellow to access your acount"),
        rx.divider(width="15%"),
        render_input_field(
            title="Email", is_password=False,
            value=LoginState.email, update=LoginState.update_email,
        ),
        render_input_field(
            title="Password", is_password=True,
            value=LoginState.password, update=LoginState.update_password,
        ),
        render_submit_button(
            name="Login!", event=LoginState.void_event
        ),
        *[rx.spacer() for _ in range(2)],
        rx.text(
            "Don't have an account? Click ",
            rx.link("here", href="/register"),
            "."
        ),
        rx.spacer(),
        spacing="2",
        style=auth_pages_stylesheet,
    )
