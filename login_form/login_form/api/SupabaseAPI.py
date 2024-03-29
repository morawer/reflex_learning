import os
from dotenv import load_dotenv
from supabase import create_client, Client


class SupabaseAPI:
    load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        self.supabase: Client = create_client(
            self.SUPABASE_KEY, self.SUPABASE_KEY)
