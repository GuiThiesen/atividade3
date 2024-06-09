import sys
from models.models_psycopg import Order

class OrderView:
    @staticmethod
    def get_order_from_args():
        if len(sys.argv) != 5:
            print("Uso: python main.py <customer_name> <employee_name> <order_date> <items_str>")
            print("Exemplo: python main.py 'Around the Horn' 'Andrew Fuller' '2024-06-09' '1,2,10.0;2,1,20.0'")
            sys.exit(1)
        
        customer_name = sys.argv[1]
        employee_name = sys.argv[2]
        order_date = sys.argv[3]
        items_str = sys.argv[4]
        items = items_str.split(';')

        return Order(customer_name, employee_name, order_date, items)