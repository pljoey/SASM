import pymysql

class MariaDBImplementation:

    def __init__(self):
        self.HOST = 'sasm-instance.cjweucaqyz2t.us-east-2.rds.amazonaws.com'
        self.USER = 'admin'
        self.PASSWORD = 'SASMpass'
        self.DATABASE = 'SASM'

    def _fetch_version(self):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("SELECT VERSION()")
            version = cur.fetchone()
            print("Database version: {} ".format(version[0]))

    def _show_tables(self):      
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SHOW TABLES")
            tables = cur.fetchone()
            print(tables)

    def check_user(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT password FROM sasm_users WHERE username = '" + username + "'")
            user_pass = cur.fetchone()
            return user_pass

database = MariaDBImplementation()
database._fetch_version()
database._show_tables()
print(database.check_user('testUser'))
