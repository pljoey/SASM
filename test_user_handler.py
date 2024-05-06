import pytest

from User import User
from UserHandler import UserHandler

def test_view_schedule():
    handler = UserHandler()
    handler.aUser = User("test")
    handler.aUser.set_current_schedule(["IT 168"])
    assert handler.view_schedule() == ["IT 168"]