import asyncio
import reflex as rx
from login_form.api.api import all_users, create_user, match_user
from login_form.model.Users import User


class State(rx.State):
    def void_event(self): ...


class LoginState(State):
    email: str
    password: str
    users_info: list[User] = []
    user_exist: bool = False
    is_query_complete: bool = False

    def print_variables(self):
        print(self.email, self.password)
        self.email = ""
        self.password = ""

    def update_email(self, email):
        self.email = email

    def update_password(self, password):
        self.password = password

    async def query_all_users(self):
        self.users_info = await all_users()

    async def query_single_user(self):
        self.user_exist = False
        self.is_query_complete = False

        await asyncio.sleep(1)  # Elimina esto en producción
        self.user_exist = await match_user(self.email, self.password)
        self.is_query_complete = True
        print("User exists:", self.user_exist)

    def delete_table(self):
        self.users_info = []


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

    async def make_user(self):
        self.test = await create_user(self.email, self.password)
