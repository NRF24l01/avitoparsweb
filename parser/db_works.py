import psycopg2


class DataBaseConnector:
    def __init__(self, dbname: str, username: str, password: str, host: str, port: int = 5432):
        """

        :param dbname: database name
        :param username: username
        :param password: password
        :param host: host with postegre
        :param port: port(usually 5432)
        """
        self.dbname = dbname
        self.user = username
        self.password = password
        self.host = host
        self.port = port

        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            # пытаемся подключиться к базе данных
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)
            self.cursor = self.conn.cursor()
        except Exception as er:
            raise er

    def insert(self, into: str, columns: tuple, values: tuple):
        if self.cursor:
            self.cursor.execute("inser")
