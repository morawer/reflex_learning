from .SupabaseAPI import SupabaseAPI
from login_form.model.Users import User
from login_form.tools.bcrypt import hash_password

SUPABASE_API = SupabaseAPI()

email: str
password: str
username: str


async def all_users() -> list[User]:
    return SUPABASE_API.query_all_users()


async def match_user(email, password) -> bool:
    return SUPABASE_API.query_single_user(email, password)


async def create_user(email, password, username):
    password_hashed = hash_password(password)
    return SUPABASE_API.insert_user(email, password_hashed.decode("utf-8"), username)
