from utils import average


def test_average():
    assert average([2, 4]) == 3


def test_average_empty():
    assert average([]) == 0
