# controllers/controller.py
from dao.dao_psycopg import PedidoDAO as PedidoDAOPsycopg
from dao.dao_sqlalchemy import PedidoDAO as PedidoDAOSQLAlchemy

class PedidoController:
    def __init__(self, dao_type='psycopg', db_config=None, db_url=None):
        if dao_type == 'psycopg':
            self.dao = PedidoDAOPsycopg(db_config)
        elif dao_type == 'sqlalchemy':
            self.dao = PedidoDAOSQLAlchemy(db_url)

    def inserir_pedido(self, pedido):
        self.dao.inserir_pedido(pedido)

    def relatorio_pedido(self, pedido_id):
        return self.dao.relatorio_pedido(pedido_id)

    def relatorio_ranking(self, start_date, end_date):
        return self.dao.relatorio_ranking(start_date, end_date)

    def close(self):
        self.dao.close()
