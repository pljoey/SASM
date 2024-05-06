import pytest
from CourseHandler import CourseHandler
from Course import Course

def test_add_custom_course_with_invalid_day_format():
    handler = CourseHandler()
    result = handler.add_custom_course("test","10:00 p", "11:00 p", "M/Fr/A/")
    assert result == False

def test_add_custom_course_with_invalid_start_time_format():
    handler = CourseHandler()
    result = handler.add_custom_course("test","10:00 qp", "11:00 p", "M/Tu/")
    assert result == False

def test_add_custom_course_with_invalid_end_time_format():
    handler = CourseHandler()
    result = handler.add_custom_course("test","10:15 a", "11:ss a", "Th/F")
    assert result == False

def test_add_custom_course_with_valid_format():
    handler = CourseHandler()
    result = handler.add_custom_course("test","10:15 a", "11:34 a", "M/Tu/W/Th/F/")
    assert result == True