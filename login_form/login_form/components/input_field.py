import reflex as rx
from login_form.styles import input_stylesheet


def render_input_field(
    title: str,
    is_password: bool,
    value: rx.Var,
    update: rx.State
):
    return rx.vstack(
        rx.text(title),
        rx.input(
            value=value, on_change=update,
            type="password" if is_password else "text",
        ),
        spacing="1",
        padding="0rem 6rem",
        style=input_stylesheet,

    )
