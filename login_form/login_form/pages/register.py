import reflex as rx
from login_form.styles import auth_pages_stylesheet
from login_form.components.input_field import render_input_field
from login_form.components.button import render_submit_button
from login_form.states import RegisterState


@rx.page(route="/register", title="Welcome to my page!")
def register():
    return rx.vstack(
        rx.hstack(
            rx.icon("sun-moon"),
            width="100%",
            justify_content="end",
            padding="1em"
        ),
        rx.spacer(),
        rx.heading(
            "Welcome to my page!", size="9",
            transition="all 550ms ease"
        ),
        rx.text("Create an acount to get started"),
        rx.divider(width="15%"),
        render_input_field(
            title="Username", icon="user", is_password=False,
            value=RegisterState.username, update=RegisterState.update_username,
        ),
        render_input_field(
            title="Email", icon="mail", is_password=False,
            value=RegisterState.email, update=RegisterState.update_email,
        ),
        render_input_field(
            title="Password", icon="key-square", is_password=True,
            value=RegisterState.password, update=RegisterState.update_password,
        ),
        render_submit_button(
            name="Create an account!",
            color="green",
            event=RegisterState.make_user(
                RegisterState.email,
                RegisterState.password,
                RegisterState.username
            )
        ),
        *[rx.spacer() for _ in range(1)],
        rx.text(
            "Already have an account? Click ",
            rx.link("here", href="/"),
            "."
        ),
        rx.spacer(),
        spacing="1",
        style=auth_pages_stylesheet,
    )
