import pytest

from Schedule import Schedule
from User import User
from UserHandler import UserHandler

def test_view_schedule_filled():
    handler = UserHandler()
    handler.aUser = User("test")
    handler.aUser.set_current_schedule(["IT 168"])
    assert handler.view_schedule() == ["IT 168"]

def test_view_schedule_empty():
    handler = UserHandler()
    handler.aUser = User("test")
    assert handler.view_schedule() == None

def test_create_schedule_tests_true():
    handler = UserHandler()
    handler.aUser = User("test")
    assert handler.create_schedule() == True