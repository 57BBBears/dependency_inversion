from uuid import uuid4

from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order import Order, OrderRepository
from app.core.product.product import ProductRepository
from app.core.user.user import UserRepository


class OrderService:
    UserRepository: UserRepository
    ProductRepository: ProductRepository
    OrderRepository: OrderRepository

    @classmethod
    def create(cls, request: CreateOrderRequest) -> None:
        _user = cls.UserRepository.find(request.user_id)
        _product = cls.ProductRepository.find(request.product_id)

        if _user.balance < _product.price:
            raise RuntimeError("Not enough balance")

        _order = Order(uuid4(), _user.id, _product.id)
        cls.OrderRepository.create(_order)
