from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'northwind'}
    
    customer_id = Column('customerid', String, primary_key=True)
    company_name = Column('companyname', String, nullable=False)
    contact_name = Column('contactname', String)
    contact_title = Column('contacttitle', String)
    address = Column('address', String)
    city = Column('city', String)
    region = Column('region', String)
    postal_code = Column('postalcode', String)
    country = Column('country', String)
    phone = Column('phone', String)
    fax = Column('fax', String)

class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'northwind'}
    
    employee_id = Column('employeeid', Integer, primary_key=True)
    last_name = Column('lastname', String, nullable=False)
    first_name = Column('firstname', String, nullable=False)
    title = Column('title', String)
    title_of_courtesy = Column('titleofcourtesy', String)
    birth_date = Column('birthdate', Date)
    hire_date = Column('hiredate', Date)
    address = Column('address', String)
    city = Column('city', String)
    region = Column('region', String)
    postal_code = Column('postalcode', String)
    country = Column('country', String)
    home_phone = Column('homephone', String)
    extension = Column('extension', String)
    notes = Column('notes', String)
    reports_to = Column('reportsto', Integer, ForeignKey('northwind.employees.employeeid'))
    
    manager = relationship("Employee", remote_side=[employee_id])

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'northwind'}
    
    product_id = Column('productid', Integer, primary_key=True)
    product_name = Column('productname', String, nullable=False)
    supplier_id = Column('supplierid', Integer, ForeignKey('northwind.suppliers.supplierid'))
    category_id = Column('categoryid', Integer, ForeignKey('northwind.categories.categoryid'))
    quantity_per_unit = Column('quantityperunit', String)
    unit_price = Column('unitprice', Float)
    units_in_stock = Column('unitsinstock', Integer)
    units_on_order = Column('unitsonorder', Integer)
    reorder_level = Column('reorderlevel', Integer)
    discontinued = Column('discontinued', Integer)
    
    supplier = relationship("Supplier")
    category = relationship("Category")

class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}
    
    order_id = Column('orderid', Integer, primary_key=True)
    customer_id = Column('customerid', String, ForeignKey('northwind.customers.customerid'))
    employee_id = Column('employeeid', Integer, ForeignKey('northwind.employees.employeeid'))
    order_date = Column('orderdate', Date)
    required_date = Column('requireddate', Date)
    shipped_date = Column('shippeddate', Date)
    shipper_id = Column('shipperid', Integer, ForeignKey('northwind.shippers.shipperid'))
    freight = Column('freight', Float)
    ship_name = Column('shipname', String)
    ship_address = Column('shipaddress', String)
    ship_city = Column('shipcity', String)
    ship_region = Column('shipregion', String)
    ship_postal_code = Column('shippostalcode', String)
    ship_country = Column('shipcountry', String)
    
    customer = relationship("Customer")
    employee = relationship("Employee")
    shipper = relationship("Shipper")

class OrderDetail(Base):
    __tablename__ = 'order_details'
    __table_args__ = {'schema': 'northwind'}
    
    order_id = Column('orderid', Integer, ForeignKey('northwind.orders.orderid'), primary_key=True)
    product_id = Column('productid', Integer, ForeignKey('northwind.products.productid'), primary_key=True)
    unit_price = Column('unitprice', Float, nullable=False)
    quantity = Column('quantity', Integer, nullable=False)
    discount = Column('discount', Float, nullable=False)
    
    order = relationship("Order")
    product = relationship("Product")

class Supplier(Base):
    __tablename__ = 'suppliers'
    __table_args__ = {'schema': 'northwind'}
    
    supplier_id = Column('supplierid', Integer, primary_key=True)
    company_name = Column('companyname', String, nullable=False)
    contact_name = Column('contactname', String)
    contact_title = Column('contacttitle', String)
    address = Column('address', String)
    city = Column('city', String)
    region = Column('region', String)
    postal_code = Column('postalcode', String)
    country = Column('country', String)
    phone = Column('phone', String)
    fax = Column('fax', String)
    home_page = Column('homepage', String)

class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'northwind'}
    
    category_id = Column('categoryid', Integer, primary_key=True)
    category_name = Column('categoryname', String, nullable=False)
    description = Column('description', String)
    picture = Column('picture', String)

class Shipper(Base):
    __tablename__ = 'shippers'
    __table_args__ = {'schema': 'northwind'}
    
    shipper_id = Column('shipperid', Integer, primary_key=True)
    company_name = Column('companyname', String, nullable=False)
    phone = Column('phone', String)

class OrderArgs:
    def __init__(self, customer_name, employee_name, order_date, items):
        self.customer_name = customer_name
        self.employee_name = employee_name
        self.order_date = order_date
        self.items = items
