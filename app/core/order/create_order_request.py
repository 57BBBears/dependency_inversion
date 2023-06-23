from dataclasses import dataclass

from uuid import UUID


@dataclass
class CreateOrderRequest:
    """
    Request data class, which user send to create product order
    """

    user_id: UUID
    product_id: UUID
