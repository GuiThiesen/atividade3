from controllers.controller_sqlalchemy import OrderController
from views.view_sqlalchemy import OrderView

def main():
    db_url = 'postgresql://postgres:1234@localhost/northwind'
    
    order = OrderView.get_order_from_args()
    controller = OrderController(db_url)
    try:
        controller.process_order(order)
        print("Pedido registrado com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
