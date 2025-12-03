from lib.counter import *

def test_counter_count_0():
    counter = Counter()
    result = counter.report()
    assert result == 'Counted to 0 so far.'

def test_counter_count_to_3():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == 'Counted to 3 so far.'