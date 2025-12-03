from lib.string_builder import *

# testing returning the empty string
def test_string_builder_returns_0():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ''

# testing adding 'hello' to the string and returning it
def test_string_builder_returns_hello():
    string_builder = StringBuilder()
    string_builder.add('hello')
    result = string_builder.output()
    assert result == 'hello'

# testing adding 'hello' and '824' to the string and returning it
def test_string_builder_returns_hello_and_num():
    string_builder = StringBuilder()
    string_builder.add('hello')
    string_builder.add('842')
    result = string_builder.output()
    assert result == 'hello842'