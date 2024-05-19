import reflex as rx
from login_form.styles import auth_pages_stylesheet
from login_form.components.input_field import render_input_field
from login_form.components.button import render_submit_button
from login_form.states import LoginState


@rx.page(route="/", title="Welcome Back!")
def login():
    return rx.vstack(
        rx.hstack(
            rx.icon("sun-moon"),
            width="100%",
            justify_content="end",
            padding="1em"
        ),
        rx.spacer(),
        rx.heading(
            "Welcome Back!", size="9",
            transition="all 550ms ease"
        ),
        rx.text("Sign in bellow to access your acount"),
        rx.divider(width="15%"),
        render_input_field(
            title="Email", icon="mail", is_password=False,
            value=LoginState.email, update=LoginState.update_email,
        ),
        render_input_field(
            title="Password", icon="key-square", is_password=True,
            value=LoginState.password, update=LoginState.update_password,
        ),
        rx.dialog.root(
            rx.dialog.trigger(
                render_submit_button(
                    name="Verify user", color="green", event=LoginState.query_single_user
                )
            ),
            rx.cond(
                LoginState.is_query_complete,
                rx.cond(
                    LoginState.user_exist,
                    rx.dialog.content(
                        rx.dialog.title("User Exists"),
                        rx.dialog.description(
                            "This user exists in the system.",
                        ),
                        rx.dialog.close(
                            rx.button("Close Dialog", size="3"),
                        ),
                    ),
                    rx.dialog.content(
                        rx.dialog.title("User Not Found"),
                        rx.dialog.description(
                            "This user does not exist in the system.",
                        ),
                        rx.dialog.close(
                            rx.button("Close Dialog", size="3"),
                        ),
                    )
                )

            )

        ),
        rx.dialog.root(
            rx.dialog.trigger(
                render_submit_button(
                    name="Show a table of users", color="red", event=LoginState.query_all_users()
                ),
            ),
            rx.dialog.content(
                rx.dialog.title("Users"),
                rx.dialog.description(
                    "Database of users registered",
                ),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Username"),
                            rx.table.column_header_cell("Email"),
                            rx.table.column_header_cell("Password"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(
                            LoginState.users_info,
                            lambda item: rx.table.row(
                                rx.table.cell(item.username),
                                rx.table.cell(item.email),
                                rx.table.cell(item.password),
                            ),
                        )
                    ),
                ),
                rx.dialog.close(
                    rx.button("Close", size="2"),
                )

            ),
        ),

        render_submit_button(
            name="Delete table", color="blue", event=LoginState.delete_table()
        ),

        * [rx.spacer() for _ in range(2)],
        rx.text(
            "Don't have an account? Click ",
            rx.link("here", href="/register"),
            "."
        ),
        rx.spacer(),
        spacing="1",
        style=auth_pages_stylesheet,
    )
