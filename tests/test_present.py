import pytest
from lib.present import *

def test_wrapped_twice():
    # Make a new present object
    # Call wrap method and add contents
    # Prepare to capture error message
    # Call wrap method and add contents
    # Assert captured message is equal to expcected error message
    
    present = Present()
    present.wrap("Candy cane")
    with pytest.raises(Exception) as e:
        present.wrap("Candy cane")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_without_wrapping():
    # Make a new present object
    # Prepare to capture error message
    # Call unwrap method 
    # Assert captured message is equal to expcected error message   

    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."    


# def test_wrapped_once_and_unwrapped():
#     # Make a new present object
#     # Call wrap method and add contents
#     # Call present.contents
#     # Call unwrap method
#     present = Present()
#     present.wrap("Candy cane")
#     print(present.contents())
#     present.unwrap()