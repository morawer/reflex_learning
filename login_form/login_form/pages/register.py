import reflex as rx
from login_form.styles import auth_pages_stylesheet
from login_form.components.input_field import render_input_field
from login_form.components.button import render_submit_button
from login_form.states import RegisterState


@rx.page(route="/register")
def register():
    return rx.vstack(
        rx.hstack(
            rx.icon("sun-moon"),
            width="100%",
            justify_content="end",
        ),
        rx.spacer(),
        rx.heading(
            "Welcome to my page!", size="9",
            transition="all 550ms ease"
        ),
        rx.text("Create an acount to get started"),
        rx.divider(width="15%"),
        render_input_field(
            title="Username", is_password=False,
            value=RegisterState.username, update=RegisterState.update_username,
        ),
        render_input_field(
            title="Email", is_password=False,
            value=RegisterState.email, update=RegisterState.update_email,
        ),
        render_input_field(
            title="Password", is_password=True,
            value=RegisterState.password, update=RegisterState.update_password,
        ),
        render_submit_button(
            name="Create account!", event=RegisterState.void_event
        ),
        *[rx.spacer() for _ in range(2)],
        rx.text(
            "Already have an account? Click ",
            rx.link("here", href="/"),
            "."
        ),
        rx.spacer(),
        spacing="2",
        style=auth_pages_stylesheet,
    )
