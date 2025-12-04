from lib.password_checker import *
import pytest

def test_for_more_than_8_password():
    password_checker = PasswordChecker()
    result = password_checker.check('ValidPassword')
    assert result == True

def test_for_exactly_8_password():
    password_checker = PasswordChecker()
    result = password_checker.check('12345678')
    assert result == True

def test_for_less_than_8_passowrd():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('Invalid')    
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."