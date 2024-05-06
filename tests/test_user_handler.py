import pytest
from UserHandler import UserHandler
from User import User
from Schedule import Schedule

def test_view_schedule():
    handler = UserHandler()
    handler.aSched = Schedule("test_sched",["IT 168"])
    handler.aUser = User("test")
    handler.aUser.set_current_schedule(handler.aSched)
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

def test_create_new_user_and_login():
    handler = UserHandler()
    handler.create_user('testing_user', 'test_pass')
    login_result = handler.login('testing_user', 'test_pass')
    handler.delete_user('test_pass')
    assert login_result == True
    
def test_create_new_user_with_reused_user():
    handler = UserHandler()
    handler.create_user('testing_user', 'test_pass')
    result = handler.create_user('testing_user', 'test_pass')
    handler.login('testing_user', 'test_pass')
    handler.delete_user('test_pass')
    assert result == False

def test_login_with_wrong_pass():
    handler = UserHandler()
    handler.create_user('testing_user', 'test_pass')
    login_result = handler.login('testing_user', 'test_pass')
    handler.delete_user('test_pass')
    assert login_result == False

def test_logout():
    handler = UserHandler()
    handler.create_user('testing_user', 'test_pass')
    handler.login('testing_user', 'test_pass')
    logout_result = handler.logout()
    assert logout_result == False