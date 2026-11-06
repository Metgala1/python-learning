def transfer_money(connection, sender_id, receiver_id, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")

    try:
        with connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE accounts
                SET balance = balance - ?
                WHERE id = ?
                AND balance >= ?
                """,
                (amount, sender_id, amount)
            )

            if cursor.rowcount != 1:
                raise ValueError("Insufficient funds or invalid sender")

            cursor.execute(
                """
                UPDATE accounts
                SET balance = balance + ?
                WHERE id = ?
                """,
                (amount, receiver_id)
            )

            if cursor.rowcount != 1:
                raise ValueError("Invalid receiver")

    except Exception:
        raise