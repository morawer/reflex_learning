import os
from dotenv import load_dotenv
from supabase import create_client, Client
from login_form.model.Users import User


class SupabaseAPI:

    load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    email: str
    password: str

    def __init__(self) -> None:
        self.supabase: Client = create_client(
            self.SUPABASE_URL, self.SUPABASE_KEY)
        print(self.supabase)

    def query_all_users(self):
        response = self.supabase.table("login_table").select("*").execute()
        users_data = []

        if len(response.data) > 0:
            for user in response.data:
                users_data.append(
                    User(
                        email=user["email"],
                        password=user["password"]
                    )
                )
        return users_data

    def query_single_user(self, email):
        response = self.supabase.from_("login_table").select(
            "email", "password").eq("email", email).execute()
        print(response)

    def insert_user(self, email, password):
        response = self.supabase.table("login_table").insert(
            {"email": email, "password": password}).execute()
        print(response)
