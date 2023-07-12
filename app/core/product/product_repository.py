from typing import Protocol
from uuid import UUID

from app.core.product.product import Product


class ProductRepository(Protocol):
    def find(self, product_id: UUID) -> Product:
        """Get product by id"""
        ...
