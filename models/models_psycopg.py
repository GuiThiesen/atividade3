# models/models_psycopg.py

class Cliente:
    def __init__(self, cliente_id, nome):
        self.cliente_id = cliente_id
        self.nome = nome


class Funcionario:
    def __init__(self, funcionario_id, nome):
        self.funcionario_id = funcionario_id
        self.nome = nome


class Pedido:
    def __init__(self, pedido_id, cliente_id, funcionario_id, data_pedido):
        self.pedido_id = pedido_id
        self.cliente_id = cliente_id
        self.funcionario_id = funcionario_id
        self.data_pedido = data_pedido


class ItemPedido:
    def __init__(self, item_id, pedido_id, produto, quantidade, preco):
        self.item_id = item_id
        self.pedido_id = pedido_id
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
