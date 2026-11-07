class PaymentRespository:
    def create(self, connection, order_id, amount):
        cursor = connection.execute("""
                                    INSERT INTO payments (order_id , amount)
                                    VALUES (? , ?)
                                    """, (order_id , amount))
        
        return cursor.lastrowid