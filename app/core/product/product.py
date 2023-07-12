from dataclasses import dataclass

from uuid import UUID


@dataclass
class Product:
    id: UUID
    title: str
    price: int
