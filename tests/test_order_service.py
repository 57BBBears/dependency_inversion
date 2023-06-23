import pytest

from uuid import uuid4

from app.core.user.user import User
from app.core.product.product import Product
from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order_service import OrderService, order


def test_order_service(mocker):
    user = User(uuid4(), "Pete", 100)
    product = Product(uuid4(), "Bread", 100)
    mocker.patch(
        "app.core.order.order_service.user.UserRepositoryImpl.find",
        new=mocker.Mock(return_value=user),
    )
    mocker.patch(
        "app.core.order.order_service.product.ProductRepositoryImpl.find",
        new=mocker.Mock(return_value=product),
    )
    spy = mocker.spy(order.OrderRepositoryImpl, "create")

    order_request = CreateOrderRequest(user_id=uuid4(), product_id=uuid4())
    OrderService.create(order_request)

    spy.assert_called_once()

    product.price = user.balance + 1
    with pytest.raises(RuntimeError):
        OrderService.create(order_request)
