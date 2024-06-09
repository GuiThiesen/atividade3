from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models.models_sqlalchemy import Customer, Employee, Product, Order, OrderDetail, Base

class OrderManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_customer(self, customer_name):
        return self.session.query(Customer).filter_by(company_name=customer_name).first()

    def get_employee(self, employee_name):
        first_name, last_name = employee_name.split(' ', 1)
        return self.session.query(Employee).filter_by(first_name=first_name, last_name=last_name).first()

    def get_product(self, product_id):
        return self.session.query(Product).filter_by(product_id=product_id).first()

    def get_next_order_id(self):
        max_order_id = self.session.query(func.max(Order.order_id)).scalar()
        return max_order_id + 1 if max_order_id else 1

    def insert_order(self, customer_id, employee_id, order_date):
        order_id = self.get_next_order_id()
        new_order = Order(order_id=order_id, customer_id=customer_id, employee_id=employee_id, order_date=order_date)
        self.session.add(new_order)
        self.session.commit()
        return order_id

    def insert_order_details(self, order_id, items):
        for item in items:
            product_id, quantity, unit_price = item.split(',')
            product = self.get_product(int(product_id))
            if not product:
                raise ValueError(f"Produto com ID {product_id} não existe.")
            new_order_detail = OrderDetail(order_id=order_id, product_id=int(product_id), quantity=int(quantity), unit_price=float(unit_price), discount=0)
            self.session.add(new_order_detail)
        self.session.commit()

    def close_connection(self):
        self.session.close()
