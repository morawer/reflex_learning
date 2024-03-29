from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()


async def users():
    return SUPABASE_API.query_users()


async def create_user():
    return SUPABASE_API.insert_user()
