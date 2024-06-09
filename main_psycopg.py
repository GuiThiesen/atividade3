# main_psycopg.py
from controllers.controller import PedidoController
from views.view import obter_dados_pedido, mostrar_relatorio_pedido, mostrar_relatorio_ranking

db_config = {
    'dbname': 'northwind',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5432
}

controller = PedidoController(dao_type='psycopg', db_config=db_config)

# Inserir um novo pedido
pedido = obter_dados_pedido()
controller.inserir_pedido(pedido)

# Gerar relatório de um pedido
pedido_id = 1  # Exemplo de ID de pedido
relatorio = controller.relatorio_pedido(pedido_id)
mostrar_relatorio_pedido(relatorio)

# Gerar ranking dos funcionários
start_date = '2024-01-01'
end_date = '2024-06-01'
relatorio = controller.relatorio_ranking(start_date, end_date)
mostrar_relatorio_ranking(relatorio)

controller.close()
