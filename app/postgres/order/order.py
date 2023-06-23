from app.core.order.order import Order


class OrderRepositoryImpl:
    @classmethod
    def create(cls, order: Order) -> None:
        # insert into order (id, user_id, product_id) values (?, ?, ?)
        ...
