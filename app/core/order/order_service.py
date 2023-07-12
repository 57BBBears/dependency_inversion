from uuid import uuid4

from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order import Order
from app.core.order.create_order_observer import CreateOrderObserver
from app.core.order.create_order_events import CreateOrderEvents
from app.core.order.order_repository import OrderRepository
from app.core.product.product_repository import ProductRepository
from app.core.user.user_repository import UserRepository


class OrderService:
    user_repository: UserRepository
    product_repository: ProductRepository
    order_repository: OrderRepository
    observers: list[CreateOrderObserver]

    @classmethod
    def create(cls, request: CreateOrderRequest) -> None:
        start_event = CreateOrderEvents.start(request)
        for observer in cls.observers:
            observer.on_start(start_event)

        _user = cls.user_repository.find(request.user_id)
        _product = cls.product_repository.find(request.product_id)

        if _user.balance < _product.price:
            raise RuntimeError("Not enough balance")

        _order = Order(uuid4(), _user.id, _product.id)
        cls.order_repository.create(_order)

        end_event = CreateOrderEvents.end(request, _user, _product, _order)
        for observer in cls.observers:
            observer.on_end(end_event)
