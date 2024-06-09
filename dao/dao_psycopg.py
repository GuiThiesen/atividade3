import psycopg2

class OrderManager:
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)
        self.cursor = self.conn.cursor()

    def get_customer(self, customer_name):
        query = "SELECT c.customerid FROM northwind.customers c WHERE c.companyname = %s"
        self.cursor.execute(query, (customer_name,))
        customer = self.cursor.fetchone()
        return customer[0] if customer else None

    def get_employee(self, employee_name):
        firstname, lastname = employee_name.split(' ', 1)
        query = "SELECT e.employeeid FROM northwind.employees e WHERE e.firstname = %s AND e.lastname = %s"
        self.cursor.execute(query, (firstname, lastname))
        employee = self.cursor.fetchone()
        return employee[0] if employee else None

    def get_product(self, product_id):
        query = "SELECT p.productid FROM northwind.products p WHERE p.productid = %s"
        self.cursor.execute(query, (product_id,))
        product = self.cursor.fetchone()
        return product[0] if product else None

    def get_next_order_id(self):
        query = "SELECT MAX(o.orderid) FROM northwind.orders o"
        self.cursor.execute(query)
        max_order_id = self.cursor.fetchone()[0]
        return max_order_id + 1 if max_order_id else 1

    def insert_order(self, customer_id, employee_id, order_date):
        order_id = self.get_next_order_id()
        query = "INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (order_id, customer_id, employee_id, order_date))
        self.conn.commit()
        return order_id

    def insert_order_details(self, order_id, items):
        for item in items:
            product_id, quantity, unit_price = item.split(',')
            product = self.get_product(int(product_id))
            if not product:
                raise ValueError(f"Produto com ID {product_id} não existe.")
            query = "INSERT INTO northwind.order_details (orderid, productid, quantity, unitprice, discount) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (order_id, int(product_id), int(quantity), float(unit_price), 0))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
