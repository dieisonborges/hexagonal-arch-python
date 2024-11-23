import sqlite3
from ports.order_repository import OrderRepository

class SQLiteOrderRepository(OrderRepository):
    """Adaptador para acessar o banco SQLite."""

    def __init__(self, db_path):
        self.db_path = db_path

    def fetch_order_items(self, order_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT price, quantity FROM order_items WHERE order_id = ?", (order_id,))
        items = [{"price": price, "quantity": quantity} for price, quantity in cursor.fetchall()]
        conn.close()
        return items
