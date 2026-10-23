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



    def __del__(self):
        if self.conn:
            self.conn.close()
