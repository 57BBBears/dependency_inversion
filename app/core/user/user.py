from dataclasses import dataclass

from typing import Protocol
from uuid import UUID


@dataclass
class User:
    id: UUID
    name: str
    balance: int


class UserRepository(Protocol):
    def find(self, user_id: UUID) -> User:
        """Get user by id"""
