import psycopg


class DB_Helper:
    def __init__(self, host=None, database=None, user=None):
        self._conn = psycopg.connect(host=host, dbname=database, user=user)
        self._conn.autocommit = False
        self._host = host
        self._database = database
        self._user = user
        self._cursor = self._conn.cursor()

    def __str__(self):
        return f"host {self._host}, database {self._database}, user {self._user}"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self, commit=False):
        if commit:
            self.commit()
        else:
            self.rollback()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql, params=None, return_data=False):
        if return_data:
            self.cursor.execute(sql, params or ())
            return self.fetchall()
        else:
            self.cursor.execute(sql, params or ())
