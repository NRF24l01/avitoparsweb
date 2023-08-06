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

    def insert(self, table: str, columns: tuple, values: tuple):
        if self.cursor:
            colms = ", ".join(columns)
            vals_q = ", ".join(self._genq(values))
            self.cursor.execute(f"INSERT INTO public.{table} ({colms}) VALUES({vals_q})", values)
            self.conn.commit()
        else:
            raise ConnectionError

    def select(self, table: str, column: tuple, where: tuple):
        if self.cursor:
            pass
        else:
            raise ConnectionError

    def _genq(self, values: tuple) -> tuple:
        res = []
        for i in range(len(values)):
            res.append("%s")
        return tuple(res)

    def stop(self):
        if self.cursor or self.conn:
            self.cursor.close()  # закрываем курсор
            self.conn.close()  # закрываем соединение

    def __del__(self):
        self.stop()


if __name__ == "__main__":
    db_control = DataBaseConnector()
    db_control.connect()
    db_control.insert("keys", ("key", "usages"), ("test", "100"))
    db_control.stop()
