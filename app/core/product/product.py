from dataclasses import dataclass

from uuid import UUID
from typing import Protocol


@dataclass
class Product:
    id: UUID
    title: str
    price: int


class ProductRepository(Protocol):
    def find(self, product_id: UUID) -> Product:
        """Get product by id"""
