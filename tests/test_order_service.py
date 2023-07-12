import pytest

from uuid import uuid4

from app.core.order.create_order_request import CreateOrderRequest
from app.core.order.order import Order
from app.core.order.order_service import OrderService
from app.core.product.product import Product
from app.core.user.user import User
from app.postgres.order.create_order_observer import CreateOrderObserverImpl
from app.core.order.create_order_events import Start, End
from app.postgres.order.order_repository import OrderRepositoryImpl
from app.postgres.user.user_repository import UserRepositoryImpl
from app.postgres.product.product_repository import ProductRepositoryImpl


def test_order_service(mocker):
    user = User(user_id := uuid4(), "Pete", 100)
    product = Product(product_id := uuid4(), "Bread", 100)
    order = Order(uuid4(), user_id, product_id)
    # mock
    mocker.patch(
        "app.core.order.order_service.Order", new=mocker.Mock(return_value=order)
    )
    UserRepositoryImpl.find = mocker.Mock(return_value=user)
    ProductRepositoryImpl.find = mocker.Mock(return_value=product)
    spy_order_repository_create = mocker.spy(OrderRepositoryImpl, "create")
    spy_create_order_on_start = mocker.spy(CreateOrderObserverImpl, "on_start")
    spy_create_order_on_end = mocker.spy(CreateOrderObserverImpl, "on_end")
    # test
    # order creation
    order_request = CreateOrderRequest(user_id=uuid4(), product_id=uuid4())
    OrderService.user_repository = UserRepositoryImpl
    OrderService.product_repository = ProductRepositoryImpl
    OrderService.order_repository = OrderRepositoryImpl
    OrderService.observers = [CreateOrderObserverImpl]
    OrderService.create(order_request)
    # results
    spy_order_repository_create.assert_called_once_with(order)
    # check observers
    start_true = Start(order_request)
    start_false = Start(CreateOrderRequest(user_id=uuid4(), product_id=uuid4()))
    end_true = End(order_request, user, product, order)
    end_false = End(order_request, user, product, Order(uuid4(), uuid4(), uuid4()))

    spy_create_order_on_start.assert_called_once_with(start_true)
    spy_create_order_on_end.assert_called_once_with(end_true)

    with pytest.raises(AssertionError):
        spy_create_order_on_start.assert_called_once_with(start_false)
        spy_create_order_on_end.assert_called_once_with(end_false)

    product.price = user.balance + 1
    with pytest.raises(RuntimeError):
        OrderService.create(order_request)
