from MariaDBImplementation import MariaDBImplementation

class DatabaseManagementFactory:
    @staticmethod
    def get_database_instance(database_type):
        if database_type == 'mariadb':
            return MariaDBImplementation.get_instance()

new_database = DatabaseManagementFactory.get_database_instance('mariadb')

print(new_database.get_user_pass('testUser'))

new_database2 = DatabaseManagementFactory.get_database_instance('mariadb')

print(new_database)
print(new_database2)
