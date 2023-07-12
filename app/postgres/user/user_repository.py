from uuid import UUID

from app.core.user.user import User


class UserRepositoryImpl:
    @classmethod
    def find(cls, user_id: UUID) -> User:
        # select * from user where user.id = ?
        ...
