from typing import Protocol

from app.core.order.create_order_events import Start, End


class CreateOrderObserver(Protocol):
    @staticmethod
    def on_start(event: Start):
        """Run processes on start up of order service."""

    @staticmethod
    def on_end(event: End):
        """Run processes at the end of order service."""
