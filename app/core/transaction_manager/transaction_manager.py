from typing import Protocol


class TransactionManager(Protocol):
    def begin(self):
        """Begin transaction."""

    def commit(self):
        """Commit transaction."""
