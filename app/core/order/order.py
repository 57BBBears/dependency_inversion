from dataclasses import dataclass

from uuid import UUID
from typing import Protocol


@dataclass
class Order:
    id: UUID
    userId: UUID
    productId: UUID


class OrderRepository(Protocol):
    def create(self, order: Order) -> None:
        """Save order data"""
