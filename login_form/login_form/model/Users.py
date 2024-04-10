import reflex as rx


class User(rx.Base):
    username: str = ""
    email: str = ""
    password: str = ""
