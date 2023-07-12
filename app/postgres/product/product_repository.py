from uuid import UUID

from app.core.product.product import Product


class ProductRepositoryImpl:
    @classmethod
    def find(cls, product_id: UUID) -> Product:
        # select * from product where product.id = ?
        ...
