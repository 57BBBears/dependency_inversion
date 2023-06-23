from uuid import uuid4

from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order import Order
from app.postgres.order import order
from app.postgres.product import product
from app.postgres.user import user


class OrderService:
    UserRepositoryImpl = user.UserRepositoryImpl
    ProductRepositoryImpl = product.ProductRepositoryImpl
    OrderRepositoryImpl = order.OrderRepositoryImpl

    @classmethod
    def create(cls, request: CreateOrderRequest) -> None:
        _user = cls.UserRepositoryImpl.find(request.user_id)
        _product = cls.ProductRepositoryImpl.find(request.product_id)

        if _user.balance < _product.price:
            raise RuntimeError("Not enough balance")

        _order = Order(uuid4(), _user.id, _product.id)
        cls.OrderRepositoryImpl.create(_order)
