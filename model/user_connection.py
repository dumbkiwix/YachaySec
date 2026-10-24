import psycopg
class UserConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=gregory password=marlon host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            if self.conn:
                self.conn.close()

    def Write(self , data):
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
        """,data)
            self.conn.commit()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute('SELECT id, name, phone FROM "user" ORDER BY id ASC')
            records = cur.fetchall()
            # Convertir las tuplas devueltas por PostgreSQL en una lista de diccionarios
            users = [{"id": row[0], "name": row[1], "phone": row[2]} for row in records]
            return users
                
    def update(self, user_id: int, data: dict):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "user" 
                SET name = COALESCE(%(name)s, name), 
                    phone = COALESCE(%(phone)s, phone) 
                WHERE id = %(id)s
            """, {**data, "id": user_id})
            self.conn.commit()

    def delete(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute('DELETE FROM "user" WHERE id = %s', (user_id,))
            self.conn.commit()


    def __del__(self):
        if self.conn:
            self.conn.close()
