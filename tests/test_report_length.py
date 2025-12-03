from lib.report_length import *

# Tests if a string with a length of 5 returns 'This string was 5 characters long.'
def test_report_lenght_returns_5():
    result = report_length('hello')
    assert result == 'This string was 5 characters long.'

# Tests if a string with a length of 0 returns 'This string was 0 characters long.'
def test_report_lenght_returns_0():
    result = report_length('')