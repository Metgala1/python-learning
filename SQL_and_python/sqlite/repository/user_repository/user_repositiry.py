from database.connection import data_connection


class UserRepository:
    
    def get_by_id(self, user_id):
        with data_connection() as connection:
            user = connection.execute("""
                                      SELECT * FROM users WHERE id = ?
                                      """, (user_id,)).fetchone()
            
            return user
        
    def fetch_all(self):
        with data_connection() as connection:
            users = connection.execute("""
                                       SELECT * FROM users
                                       """).fetchall()
            return users
    
    def create(self, name, email):
        with data_connection() as connection:
            with connection:
                connection.execute("""
                                INSERT INTO users (name, email)
                                VALUES (? , ?)
                                """, (name , email))