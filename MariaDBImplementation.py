import pymysql
from DatabaseAbstract import DatabaseAbstract

class MariaDBImplementation(DatabaseAbstract):

    _instance = None

    def __init__(self):
        self.HOST = 'sasm-instance.cjweucaqyz2t.us-east-2.rds.amazonaws.com'
        self.USER = 'admin'
        self.PASSWORD = 'SASMpass'
        self.DATABASE = 'SASM'

    @staticmethod
    def get_instance():
        if MariaDBImplementation._instance == None:
            MariaDBImplementation._instance = MariaDBImplementation()
        
        return MariaDBImplementation._instance

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

    def _gen_course_id(self, department, course_num):
        #Generating id based on numbers from course nom
        department = department.lower()

        course_id = ""

        for letter in department:
            course_id = course_id + str(ord(letter) - 96) + '0'

        course_id = course_id + str(course_num)

        return int(course_id)

    def _get_prof_id(self, professor_first, professor_last, department):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT professor_id FROM professor WHERE first_name = '{professor_first}' AND last_name = '{professor_last}' AND department = '{department}'")
            return cur.fetchone()[0]

    def _gen_section_id(self, course_id, section_num):
        return int(str(course_id) + '0' + str(section_num))
    
    def _get_schedule_id(self, user_id, schedule_name):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT schedule_id FROM schedule_name WHERE schedule_name = '{schedule_name}' AND user_id = {user_id}")
            return cur.fetchone()[0]

    def get_user_pass(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT password FROM sasm_users WHERE username = '" + username + "'")
            user_pass = cur.fetchone()
            if user_pass == None:
                return None
            return user_pass[0]
        
    def check_user(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT username FROM sasm_users WHERE username = '" + username + "'")
            username_db = cur.fetchone()
            return username_db != None
        
    def check_password(self, username, password):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT username FROM sasm_users WHERE username = '{username}' AND password = '{password}'")
            username_db = cur.fetchone()
            return username_db != None
        
    def update_password(self, username, password):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"UPDATE sasm_users SET password = " + password + "WHERE username = " + username)
            connection.commit()
        
    def create_user(self, username, hash_password):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT user_id FROM sasm_users ORDER BY user_id DESC LIMIT 1")
            last_user_id = cur.fetchone()
            last_user_id = int(last_user_id[0])
            
            new_user_id = last_user_id + 1

            cur.execute(f"INSERT INTO sasm_users (user_id, username, password) VALUES ({new_user_id}, '{username}', '{hash_password}')")
            connection.commit()

    def change_password(self, username, hash_password):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"UPDATE sasm_users SET password = '{hash_password}' WHERE username = '{username}'")
            connection.commit()

    def get_preferred_hours(self, username):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT preferred_credit_hours FROM sasm_users WHERE username = '{username}'")
            credit_hours = cur.fetchone()
            if credit_hours == None:
                return None
            return int(credit_hours[0])

    def set_preferred_hours(self, username, hours):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"UPDATE sasm_users SET preferred_credit_hours = {hours} WHERE username = '{username}'")
            connection.commit()

    def add_course(self, department, course_num, description):
        #Generating id based on numbers from course nom
        course_id = self._gen_course_id(department, course_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO course (course_id, department, course_num, description) VALUES ({course_id}, '{department}', {course_num}, '{description}')")
            connection.commit()


    def get_course_description(self, department, course_num):
        course_id = self._gen_course_id(department, course_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT description FROM course WHERE course_id = {course_id}")
            description = cur.fetchone()
            if description == None:
                return None
            return description[0]

    def add_professor(self, first_name, last_name, title, department):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute("SELECT professor_id FROM professor ORDER BY user_id DESC LIMIT 1")
            last_professor_id = cur.fetchone()
            last_professor_id = int(last_professor_id[0])
            new_professor_id = last_professor_id + 1

            cur.execute(f"INSERT INTO professor (professor_id, first_name, last_name, title, department) VALUES ({new_professor_id}, '{first_name}', '{last_name}', '{title}', '{department}')")
            connection.commit()

    def add_section(self, section_num, professor_first, professor_last, professor_dept, department, course_num, start_time, end_time, monday = False, tuesday = False, wednesday = False, thursday = False, friday = False):
        professor_id = self._get_prof_id(professor_first, professor_last, professor_dept)
        course_id = self._gen_course_id(department, course_num)
        unique_section_id = self._gen_section_id(course_id, section_num)

        #TODO: Convert times to sql time format
        start_time = start_time
        end_time = end_time

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO section (unique_id, section_id, professor_id, start_time, end_time, course_id, monday, tuesday, wednesday, thursday, friday) VALUES ({unique_section_id},{section_num}, {professor_id}, '{start_time}', '{end_time}', {course_id}, {int(monday)}, {int(tuesday)}, {int(wednesday)}, {int(thursday)}, {int(friday)})")
            connection.commit()

    #TODO: figure out how to format this
    def get_sections(self, department, course_num):
        course_id = self._gen_course_id(department, course_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT section_id FROM section WHERE course_id = {course_id}")
            sections = cur.fetchone()
            return sections

    def add_course_to_blacklist(self, username, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO blacklist (user_id, course_id) VALUES ({user_id}, {course_id})")
            connection.commit()

    def add_professor_to_blacklist(self, username, professor_first, professor_last, professor_dept):
        prof_id = self._get_prof_id(professor_first, professor_last, professor_dept)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO blacklist (user_id, professor_id) VALUES ({user_id}, {prof_id})")
            connection.commit()

    def remove_course_from_blacklist(self, username, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"DELETE FROM blacklist WHERE user_id = {user_id} AND course_id = {course_id}")
            connection.commit()

    def remove_professor_from_blacklist(self, username, professor_first, professor_last, professor_dept):
        prof_id = self._get_prof_id(professor_first, professor_last, professor_dept)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"DELETE FROM blacklist WHERE user_id = {user_id} AND professor_id = {prof_id}")
            connection.commit()

    #TODO: Figure out return type
    def get_blacklist(self, username):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT course_id, professor_id FROM blacklist WHERE user_id = {user_id}")
            blacklist = cur.fetchone()
            return blacklist

    def add_to_previous_courses(self, username, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO previous_courses (user_id, course_id) VALUES ({user_id}, {course_id})")
            connection.commit()

    def remove_from_previous_courses(self, username, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"DELETE FROM previous_courses WHERE user_id = {user_id} AND course_id = {course_id}")
            connection.commit()

    def get_previous_courses(self, username):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT course_id FROM previous_courses WHERE user_id = {user_id}")
            prev_courses = cur.fetchone()

            course_list = []

            if prev_courses == None:
                return course_list

            for prev_course in prev_courses:
                cur.execute(f"SELECT department, course_num FROM course WHERE course_id = {prev_course}")
                course_details = cur.fetchone()
                course_list.append(str(course_details[0]) +  ' ' + str(course_details[1]))

            return course_list

    def add_to_preferred_electives(self, username, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO preferred_electives (user_id, course_id) VALUES ({user_id}, {course_id})")
            connection.commit()

    def remove_from_preferred_electives(self, username, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"DELETE FROM preferred_electives WHERE user_id = {user_id} AND course_id = {course_id}")

    def get_preferred_electives(self, username):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT course_id FROM preferred_electives WHERE user_id = {user_id}")
            preferred_courses = cur.fetchone()

            course_list = []

            if preferred_courses == None:
                return course_list

            for preferred_course in preferred_courses:
                cur.execute(f"SELECT department, course_num FROM course WHERE course_id = {preferred_course}")
                course_details = cur.fetchone()
                course_list.append(str(course_details[0]) +  ' ' + str(course_details[1]))

            return course_list

    def delete_user(self, username):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"DELETE FROM preferred_electives WHERE user_id = {user_id}")
            cur.execute(f"DELETE FROM previous_courses WHERE user_id = {user_id}")
            cur.execute(f"DELETE FROM blacklist WHERE user_id = {user_id}")
            cur.execute(f"DELETE FROM sasm_users WHERE user_id = {user_id}")

            connection.commit()

    def check_for_course(self, department, course_num):
        course_id = self._gen_course_id(department, course_num)
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT * FROM course WHERE course_id = {course_id}")
            results = cur.fetchone()

            return results != None
        
    def add_course_prereqs(self, course_dept, course_num, prereq_dept, prereq_num):
        course_id = self._gen_course_id(course_dept, course_num)
        prereq_id = self._gen_course_id(prereq_dept, prereq_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO prereqs (course_id, prereq_id) VALUES ({course_id}, {prereq_id})")
            connection.commit()

    def get_course_prereqs(self, course_dept, course_num):
        course_id = self._gen_course_id(course_dept, course_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT prereq_id FROM prereqs WHERE course_id = {course_id}")
            prereqs = cur.fetchone()

            course_list = []

            if prereqs == None:
                return course_list
            
            for prereq in prereqs:
                cur.execute(f"SELECT department, course_num FROM course WHERE course_id = {prereq}")
                course_details = cur.fetchone()
                course_list.append(str(course_details[0]) +  ' ' + str(course_details[1]))

            return course_list
        
    def create_schedule(self, username, name=None):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            schedule_name = name

            if name == None:
                name_found = False
                counter = 1

                while not name_found:
                    cur.execute(f"SELECT schedule_name FROM schedule_name WHERE schedule_name = 'schedule{counter}'")
                    if cur.fetchone() == None:
                        schedule_name = 'schedule' + str(counter)
                        break
            
            cur.execute(f"SELECT schedule_id FROM schedule_name ORDER BY schedule_id DESC")
            schedule_id = cur.fetchone()

            if schedule_id == None:
                schedule_id = 1

            else:
                schedule_id = cur.fetchone()[0] + 1

            cur.execute(f"INSERT INTO schedule_name (user_id, schedule_name, schedule_id) VALUES ({user_id}, '{schedule_name}', {schedule_id})")

            connection.commit()

    
    def edit_schedule_name(self, username, old_name, new_name):
        user_id = self._get_user_id(username)
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")

            cur.execute(f"SELECT schedule_name FROM schedule_name WHERE schedule_name = '{old_name}' AND user_id = {user_id}")

            if cur.fetchone() != None:
                return False
            
            cur.execute(f"SELECT schedule_name FROM schedule_name WHERE schedule_name = '{new_name}' AND user_id = {user_id}")
            
            if cur.fetchone() != None:
                return False

            cur.execute(f"UPDATE schedule_name SET schedule_name = '{new_name}' WHERE schedule_name = '{old_name}' AND user_id = {user_id}")
            connection.commit()
            

    def delete_schedule(self, username, schedule_name):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT * FROM schedule_name WHERE user_id = {user_id} AND schedule_name = '{schedule_name}'")

            if cur.fetchone() == None:
                return False
            
            cur.execute(f"DELETE FROM schedule_name WHERE user_id = {user_id} AND schedule_name = '{schedule_name}'")
            connection.commit()

    def get_user_schedule_names(self, username):
        user_id = self._get_user_id(username)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"SELECT schedule_name FROM schedule_name WHERE user_id = {user_id}")
            return cur.fetchone()

    def add_section_to_schedule(self, username, schedule_name, course_dept, course_num, section_num):
        user_id = self._get_user_id(username)
        schedule_id = self._get_schedule_id(user_id, schedule_name)
        course_id = self._gen_course_id(course_dept, course_num)
        section_id = self._gen_section_id(course_id, section_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"INSERT INTO schedule_contents (schedule_id, unique_section_id) VALUES ({schedule_id}, {section_id})")
            connection.commit()

    def remove_section_from_schedule(self, username, schedule_name, course_dept, course_num, section_num):
        user_id = self._get_user_id(username)
        schedule_id = self._get_schedule_id(user_id, schedule_name)
        course_id = self._gen_course_id(course_dept, course_num)
        section_id = self._gen_section_id(course_id, section_num)

        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")
            cur.execute(f"DELETE FROM schedule_contents WHERE schedule_id = {schedule_id} AND unique_section_id = {section_id}")
            connection.commit()

    #TODO: Try and make this work
    def get_sections_from_schedule(self, username, schedule_name):
        connection = pymysql.connect(host=self.HOST, user=self.USER, password=self.PASSWORD, db=self.DATABASE)

        with connection:
            cur = connection.cursor()
            cur.execute("USE SASM")


#database = MariaDBImplementation()
#database._fetch_version()
#database._show_tables()
#print(database.check_user('testUser'))
#print(database.check_user('testUser1'))
#print(database.get_user_pass('testUser'))
#database.create_user('new_user','eek')
#print(database._get_user_id('testUser'))
#database.change_password('testUser', 'newPass')

#database.add_course('IT', 326, 'Test Description')

#database.add_to_previous_courses('testUser', 'IT', 326)

#print(database.get_previous_courses('testUser'))

#print(database.get_user_pass('Does Not Exist'))
