from app.db.models import UserModel
from app.api.security.auth import get_password_hash, verify_password


class UserService:
    @staticmethod
    async def create_user(user_data):
        hashed_password = get_password_hash(user_data.password)
        user = await UserModel.create_user(
            user_data.username, hashed_password, user_data.role
        )
        return user

    @staticmethod
    async def authenticate_user(username: str, password: str):
        user = await UserModel.get_user(username)
        if user and verify_password(password, user["hashed_password"]):
            return user
        return None
