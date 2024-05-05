import unittest

from SASM.User import User
from SASM.UserHandler import UserHandler

class UserControllerTest(unittest.TestCase):
    def view_schedule_test(self):
        user = User("test", ["IT 168"])
        handler = UserHandler()
        handler.view_schedule()