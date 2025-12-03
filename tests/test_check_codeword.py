from lib.check_codeword import *

def test_check_valid_codeword():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_check_close_codeword():
    result = check_codeword('hande')
    assert result == "Close, but nope."

def test_check_wrong_codeword():
    result = check_codeword('not the codeword')
    assert result == "WRONG!"