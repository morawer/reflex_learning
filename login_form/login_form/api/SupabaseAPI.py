import os
from dotenv import load_dotenv
from supabase import create_client, Client
import reflex as rx


class SupabaseAPI:

    class Inserted(rx.Base):
        id: int
        email: str
        password: str

    load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        self.supabase: Client = create_client(
            self.SUPABASE_URL, self.SUPABASE_KEY)
        print(self.supabase)

    def query_users(self):
        response = self.supabase.table("login_table").select("*").execute()
        print(response)

    def insert_user(self):
        response = self.supabase.table("login_table").insert(
            {"email": "morawer@gmail.com", "password": "12345##"}).execute()
        print(response)
