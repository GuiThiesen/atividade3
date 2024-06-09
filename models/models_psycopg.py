from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    customer_id = Column(String, primary_key=True)
    company_name = Column(String, nullable=False)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)

class Employee(Base):
    __tablename__ = 'employees'
    
    employee_id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    title = Column(String)
    title_of_courtesy = Column(String)
    birth_date = Column(Date)
    hire_date = Column(Date)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    home_phone = Column(String)
    extension = Column(String)
    notes = Column(String)
    reports_to = Column(Integer, ForeignKey('employees.employee_id'))
    
    manager = relationship("Employee", remote_side=[employee_id])

class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    quantity_per_unit = Column(String)
    unit_price = Column(Float)
    units_in_stock = Column(Integer)
    units_on_order = Column(Integer)
    reorder_level = Column(Integer)
    discontinued = Column(Integer)
    
    supplier = relationship("Supplier")
    category = relationship("Category")

class Order(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(String, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    order_date = Column(Date)
    required_date = Column(Date)
    shipped_date = Column(Date)
    ship_via = Column(Integer, ForeignKey('shippers.shipper_id'))
    freight = Column(Float)
    ship_name = Column(String)
    ship_address = Column(String)
    ship_city = Column(String)
    ship_region = Column(String)
    ship_postal_code = Column(String)
    ship_country = Column(String)
    
    customer = relationship("Customer")
    employee = relationship("Employee")
    shipper = relationship("Shipper")

class OrderDetail(Base):
    __tablename__ = 'order_details'
    
    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    unit_price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    discount = Column(Float, nullable=False)
    
    order = relationship("Order")
    product = relationship("Product")

class Supplier(Base):
    __tablename__ = 'suppliers'
    
    supplier_id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)
    home_page = Column(String)

class Category(Base):
    __tablename__ = 'categories'
    
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    description = Column(String)
    picture = Column(String)

class Shipper(Base):
    __tablename__ = 'shippers'
    
    shipper_id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    phone = Column(String)

class Order:
    def __init__(self, customer_name, employee_name, order_date, items):
        self.customer_name = customer_name
        self.employee_name = employee_name
        self.order_date = order_date
        self.items = items