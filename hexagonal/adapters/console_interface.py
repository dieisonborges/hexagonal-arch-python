from domain.order_calculator import calculate_total

def display_order_total(order_id, repository):
    """Mostra o total do pedido."""
    order_items = repository.fetch_order_items(order_id)  # Usa o adaptador de banco
    total = calculate_total(order_items)                 # Chama a lógica de negócio
    print(f"Total do pedido {order_id}: R${total:.2f}")
