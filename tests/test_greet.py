from lib.greet import *

def test_greet_returns_will():
    result = greet('Will')
    assert result == 'Hello, Will!'
