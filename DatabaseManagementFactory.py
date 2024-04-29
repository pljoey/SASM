from MariaDBImplementation import MariaDBImplementation

class DatabaseManagementFactory:
    @staticmethod
    def get_database_instance(database_type):
        if database_type == 'mariadb':
            return MariaDBImplementation.get_instance()