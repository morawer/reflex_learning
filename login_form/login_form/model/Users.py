import reflex as rx


class User(rx.Base):
    email: str = ""
    password: str = ""
