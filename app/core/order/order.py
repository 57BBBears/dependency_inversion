from dataclasses import dataclass

from uuid import UUID


@dataclass
class Order:
    id: UUID
    userId: UUID
    productId: UUID
