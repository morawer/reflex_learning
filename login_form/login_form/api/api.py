from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

email: str
password: str


async def users():
    return SUPABASE_API.query_users()


async def create_user(email, password):
    return SUPABASE_API.insert_user(email, password)
