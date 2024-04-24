import pymysql

class MariaDBImplementation:

    def __init__(self):
        self.HOST = 'sasm-instance.cjweucaqyz2t.us-east-2.rds.amazonaws.com'
        self.USER = 'admin'
        self.PASSWORD = 'SASMpass'
        self.DATABASE = 'SASM'
        self.connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

    def _fetch_version():
        with self.connection:
            cur = self.connection.cursor()
            cur.execute("SELECT VERSION()")
            version = cur.fetchone()
            print("Database version: {} ".format(version[0]))

    def _show_tables():       
        with self.connection:
            cur = self.connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SHOW TABLES")
            tables = cur.fetchone()
            print(tables)


