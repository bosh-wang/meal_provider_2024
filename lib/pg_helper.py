import psycopg2

class PGConnect:
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: int,
        dbname: str,
        schema: str,
        sslmode: str = None,
        sslcert: str = None,
        sslkey: str = None,
        sslrootcert: str = None,
    ) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.schema = schema
        self.sslmode = sslmode
        self.sslcert = sslcert
        self.sslkey = sslkey
        self.sslrootcert = sslrootcert
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.dbname,
                sslmode=self.sslmode,
                sslcert=self.sslcert,
                sslkey=self.sslkey,
                sslrootcert=self.sslrootcert,
            )
            print("Connected to PostgreSQL")
        except (Exception, psycopg2.Error) as error:
            print(f"Error while connecting to PostgreSQL: {error}")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Connection to PostgreSQL closed")

    def execute_query(self, query):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
            print("Query executed successfully")

