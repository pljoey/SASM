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

    def _get_user_id(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT user_id FROM sasm_users WHERE username = '" + username + "'")
            user_id = cur.fetchone()
            if user_id == None:
                return -1
            
            return int(user_id[0])

    def get_user_pass(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT password FROM sasm_users WHERE username = '" + username + "'")
            user_pass = cur.fetchone()
            return user_pass
        
    def check_user(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT username FROM sasm_users WHERE username = '" + username + "'")
            username_db = cur.fetchone()
            return username_db != None
        
    def create_user(self, username, hash_password):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT user_id FROM sasm_users ORDER BY user_id DESC LIMIT 1")
            last_user_id = cur.fetchone()
            last_user_id = int(last_user_id[0])
            
            new_user_id = last_user_id + 1

            cur.execute(f"INSERT INTO sasm_users (user_id, username, password) VALUES ('{new_user_id}', '{username}', '{hash_password}')")
            connection.commit()
            print(cur.fetchone())

database = MariaDBImplementation()
database._fetch_version()
database._show_tables()
print(database.check_user('testUser'))
print(database.check_user('testUser1'))
print(database.get_user_pass('testUser'))
#database.create_user('new_user','eek')
print(database._get_user_id('testUser'))
