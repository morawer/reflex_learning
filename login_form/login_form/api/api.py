from .SupabaseAPI import SupabaseAPI
from login_form.model.Users import User

SUPABASE_API = SupabaseAPI()

email: str
password: str


async def all_users() -> list[User]:
    return SUPABASE_API.query_all_users()


async def match_user(email):
    return SUPABASE_API.query_single_user(email)


async def create_user(email, password):
    return SUPABASE_API.insert_user(email, password)
