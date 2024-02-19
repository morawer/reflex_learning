import reflex as rx
from login_form.styles import input_stylesheet


def render_input_field(
    title: str,
    icon: str,
    is_password: bool,
    value: rx.Var,
    update: rx.State
):
    return rx.hstack(
        rx.icon(icon),
        rx.input(
            value=value, on_change=update,
            type="password" if is_password else "text",
            placeholder=title,
        ),
        justify_content="center",
        align_items="center",
        style=input_stylesheet,
        margin_top="0.5em"
    )
