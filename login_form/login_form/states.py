import reflex as rx
from login_form.api.api import users, create_user


class State(rx.State):
    def void_event(self): ...


class LoginState(State):
    email: str
    password: str
    test: str

    def print_variables(self):
        print(self.email, self.password)
        self.email = ""
        self.password = ""

    def update_email(self, email):
        self.email = email

    def update_password(self, password):
        self.password = password

    async def query_user(self):
        self.test = await users()

    async def make_user(self, email, password):
        self.test = await create_user(email, password)


class RegisterState(State):
    username: str
    email: str
    password: str

    def update_username(self, username):
        self.username = username

    def update_email(self, email):
        self.email = email

    def update_password(self, password):
        self.password = password
