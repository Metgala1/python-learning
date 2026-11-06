from database.connection import data_connection

class OrderRepository:
    def create(self, connection, customer_id, total):
        cursor = connection.execute(
            """
            INSERT INTO orders (customer_id, total)
            VALUES (?, ?)
            """,
            (customer_id, total)
        )

        return cursor.lastrowid
    