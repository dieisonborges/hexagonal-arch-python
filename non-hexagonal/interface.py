from orders_service import calculate_total

order_id = 1
total = calculate_total(order_id)
print(f"Total do pedido {order_id}: R${total:.2f}")
