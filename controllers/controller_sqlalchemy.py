from dao.dao_sqlalchemy import OrderManager
from models.models_sqlalchemy import OrderArgs

class OrderController:
    def __init__(self, db_url):
        self.order_manager = OrderManager(db_url)

    def process_order(self, order):
        customer = self.order_manager.get_customer(order.customer_name)
        if not customer:
            raise ValueError(f"Cliente {order.customer_name} não existe.")
        
        employee = self.order_manager.get_employee(order.employee_name)
        if not employee:
            raise ValueError(f"Funcionário {order.employee_name} não existe.")
        
        order_id = self.order_manager.insert_order(customer.customer_id, employee.employee_id, order.order_date)
        self.order_manager.insert_order_details(order_id, order.items)
        self.order_manager.close_connection()
