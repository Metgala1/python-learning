from repository import PaymentRespository, OrderRepository
from database.connection import data_connection

class OrderService:
    def __init__(self, order_respository, payment_respository, database_connection):
        self.order_respository = order_respository
        self.payment_respository = payment_respository
        self.database_connection = database_connection
        
    def place_order(self, customer_id , total):
        with self.database_connection as connection:
            with connection:
                
                order_id = self.order_respository.create(
                    connection,
                    customer_id,
                    total
                )
                
                self.payment_respository.create(
                    connection,
                    order_id,
                    total
                )
                
                return order_id

order_repository = OrderRepository()
payment_repository = PaymentRespository()
database_connection = data_connection()

order_service = OrderService(
    order_repository,
    payment_repository,
    database_connection
)

order_id = order_service.place_order(
    customer_id=1,
    total=5000
)

print("Order created:", order_id)
    