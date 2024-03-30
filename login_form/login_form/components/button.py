import reflex as rx

from login_form.styles import button_stylesheet


def render_submit_button(name: str, color: str, event: rx.State):
    return rx.hstack(
        rx.button(
            rx.text(name),
            color_scheme=color,
            on_click=event,
            width="80%",
        ),
        style=button_stylesheet,
        padding="1rem",
    )
