from app.core.order.create_order_events import Start, End
from app.postgres.transaction_manager.transaction_manager import TransactionManagerImpl


class CreateOrderObserverImpl:
    @staticmethod
    def on_start(event: Start):
        TransactionManagerImpl().begin()

    @staticmethod
    def on_end(event: End):
        TransactionManagerImpl().commit()
