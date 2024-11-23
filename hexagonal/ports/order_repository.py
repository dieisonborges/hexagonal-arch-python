# ports/order_repository.py
from abc import ABC, abstractmethod

class OrderRepository(ABC):
    """Define como obter os itens de um pedido."""
    
    @abstractmethod
    def fetch_order_items(self, order_id):
        pass
