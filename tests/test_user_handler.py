import pytest
from UserHandler import UserHandler
from User import User
from Schedule import Schedule

def test_view_schedule():
    handler = UserHandler()
    handler.aUser = User("test")
    handler.aUser.set_current_schedule(["IT 168"])
    assert handler.view_schedule() == ["IT 168"]

def test_create_schedule_for_user_with_schedule():
    handler = UserHandler()
    handler.aSched = Schedule("test_sched",["COM 212", "MAT 102"])
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.create_schedule()
    assert result == False

def test_create_schedule_for_user_without_schedule():
    handler = UserHandler()
    handler.aSched = None
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.create_schedule()
    assert result == True

def test_add_course_with_no_schedule():
    handler = UserHandler()
    handler.aSched = None
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.add_course("IT", "326")
    assert result == False

def test_add_course_with_fake_course():
    handler = UserHandler()
    handler.aSched = handler.aSched = Schedule("test_sched",["IT 326", "IT 168"])
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.add_course("IT", "999")
    assert result == False

def test_add_course_course_in_schedule():
    handler = UserHandler()
    handler.aSched = handler.aSched = Schedule("test_sched",["IT 326", "IT 168"])
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.add_course("IT", "326")
    assert result == False

def test_add_course_course_with_valid_course():
    handler = UserHandler()
    handler.aSched = handler.aSched = Schedule("test_sched",["IT 168"])
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.add_course("IT", "326")
    assert result == True

def test_remove_course_when_no_schedule():
    handler = UserHandler()
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.remove_course("IT", "326")
    assert result == False

def test_remove_course_when_not_in_schedule():
    handler = UserHandler()
    handler.aSched = handler.aSched = Schedule("test_sched",["IT 168"])
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.remove_course("IT", "326")
    assert result == False

def test_remove_course_when_in_schedule():
    handler = UserHandler()
    handler.aSched = handler.aSched = Schedule("test_sched",["IT 168"])
    handler.aUser = User("test_guy",[], handler.aSched)
    result = handler.remove_course("IT", "168")
    assert result == True
