import reflex as rx

from login_form.styles import button_stylesheet
from login_form.states import LoginState


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


async def verify_user_button():
    user_exists = await LoginState.query_single_user(LoginState.email, LoginState.password)
    rx.dialog.root(
        rx.dialog.trigger(
            render_submit_button(
                name="Verify user",
                color="green",
                event=await LoginState.query_single_user(
                    LoginState.email, LoginState.password)
            )
        ),
        rx.cond(
            LoginState.user_exist,
            rx.dialog.content(
                rx.dialog.title("EXISTEEEEEEE"),
                rx.dialog.description(
                    "This is a dialog component. You can render anything you want in here.",
                ),
                rx.dialog.close(
                    rx.button("Close Dialog", size="3"),
                ),
            ),
            rx.dialog.content(
                rx.dialog.title("NOOOOO EXISTEEEEEEE"),
                rx.dialog.description(
                    "This is a dialog component. You can render anything you want in here.",
                ),
                rx.dialog.close(
                    rx.button("Close Dialog", size="3"),
                ),
            )
        )
    ),
