import pytest

from uuid import uuid4

from app.core.user.user import User
from app.core.product.product import Product
from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order_service import OrderService
from app.postgres.user.user import UserRepositoryImpl
from app.postgres.product.product import ProductRepositoryImpl
from app.postgres.order.order import OrderRepositoryImpl


def test_order_service(mocker):
    user = User(uuid4(), "Pete", 100)
    product = Product(uuid4(), "Bread", 100)
    # mock
    UserRepositoryImpl.find = mocker.Mock(return_value=user)
    ProductRepositoryImpl.find = mocker.Mock(return_value=product)
    spy = mocker.spy(OrderRepositoryImpl, "create")

    order_request = CreateOrderRequest(user_id=uuid4(), product_id=uuid4())
    OrderService.UserRepository = UserRepositoryImpl
    OrderService.ProductRepository = ProductRepositoryImpl
    OrderService.OrderRepository = OrderRepositoryImpl
    OrderService.create(order_request)

    spy.assert_called_once()

    product.price = user.balance + 1
    with pytest.raises(RuntimeError):
        OrderService.create(order_request)
