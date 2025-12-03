from lib.gratitudes import Gratitudes

# Empty List of gratitiudes returns "Be grateful for: "
def test_unappended_gratitudes_returns_empty():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

# Adding sleep to gratitudes and formattting return "Be grateful for: sleep"
def test_adding_single_gartitide_returns_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add('sleep')
    result = gratitudes.format()
    assert result == "Be grateful for: sleep"

def test_adding_two_gartitide_returns_two_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add('sleep')
    gratitudes.add('games')
    result = gratitudes.format()
    assert result == "Be grateful for: sleep, games"