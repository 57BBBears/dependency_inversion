from uuid import uuid4

from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order_service import OrderService


if __name__ == "__main__":
    order_request = CreateOrderRequest(user_id=uuid4(), product_id=uuid4())
    OrderService.create(order_request)
