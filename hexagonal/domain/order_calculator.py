# domain/order_calculator.py

def calculate_total(order_items):
    """Calcula o total do pedido."""
    return sum(item["price"] * item["quantity"] for item in order_items)
