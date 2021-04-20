from main import *
from util import *

@RevaTest(points=10, tier=0)
def test_big_diff():
    assert big_diff([10, 3, 5, 6]) == 7
    assert big_diff([7, 2, 10, 9]) == 8
    assert big_diff([2, 10, 7, 2]) == 8
    assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3
    assert big_diff([5, -1, 7, 9]) == 10


@RevaTest(points=10, tier=0)
def test_has_22():
    assert has22([1, 2, 2]) == True
    assert has22([1, 2, 1, 2]) == False
    assert has22([2, 1, 2]) == False
    assert has22([]) == False
    assert has22([3, 3, 2, 2]) == True
