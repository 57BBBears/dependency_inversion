from typing import Protocol
from uuid import UUID

from app.core.user.user import User


class UserRepository(Protocol):
    def find(self, user_id: UUID) -> User:
        """Get user by id"""
        ...
