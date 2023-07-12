from dataclasses import dataclass

from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order import Order
from app.core.product.product import Product
from app.core.user.user import User


@dataclass
class Start:
    request: CreateOrderRequest


@dataclass
class End:
    request: CreateOrderRequest
    user: User
    product: Product
    order: Order


class CreateOrderEvents:
    @staticmethod
    def start(request: CreateOrderRequest) -> Start:
        return Start(request)

    @staticmethod
    def end(
        request: CreateOrderRequest, user: User, product: Product, order: Order
    ) -> End:
        return End(request, user, product, order)
