# models/models_sqlalchemy.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'customers'
    
    cliente_id = Column('customer_id', String, primary_key=True)
    nome = Column('company_name', String)
    
    pedidos = relationship('Pedido', back_populates='cliente')


class Funcionario(Base):
    __tablename__ = 'employees'
    
    funcionario_id = Column('employee_id', Integer, primary_key=True)
    nome = Column('first_name', String)
    
    pedidos = relationship('Pedido', back_populates='funcionario')


class Pedido(Base):
    __tablename__ = 'orders'
    
    pedido_id = Column('order_id', Integer, primary_key=True)
    cliente_id = Column('customer_id', String, ForeignKey('customers.customer_id'))
    funcionario_id = Column('employee_id', Integer, ForeignKey('employees.employee_id'))
    data_pedido = Column('order_date', Date)
    
    cliente = relationship('Cliente', back_populates='pedidos')
    funcionario = relationship('Funcionario', back_populates='pedidos')
    itens = relationship('ItemPedido', back_populates='pedido')


class ItemPedido(Base):
    __tablename__ = 'order_details'
    
    item_id = Column(Integer, primary_key=True)
    pedido_id = Column('order_id', Integer, ForeignKey('orders.order_id'))
    produto = Column('product_id', Integer, ForeignKey('products.product_id'))
    quantidade = Column('quantity', Integer)
    preco = Column('unit_price', Float)
    
    pedido = relationship('Pedido', back_populates='itens')
