import sqlite3

def calculate_total(order_id):
    """Calcula o total do pedido."""
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("SELECT price, quantity FROM order_items WHERE order_id = ?", (order_id,))
    items = cursor.fetchall()
    conn.close()

    total = sum(price * quantity for price, quantity in items)
    return total
