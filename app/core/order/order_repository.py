from typing import Protocol

from app.core.order.order import Order


class OrderRepository(Protocol):
    def create(self, order: Order) -> None:
        """Save order data"""
