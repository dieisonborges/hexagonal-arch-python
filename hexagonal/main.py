from adapters.sqlite_order_repository import SQLiteOrderRepository
from adapters.console_interface import display_order_total

# Configuração
db_path = "orders.db"
repository = SQLiteOrderRepository(db_path)

# Exibe o total do pedido
order_id = 1
display_order_total(order_id, repository)
