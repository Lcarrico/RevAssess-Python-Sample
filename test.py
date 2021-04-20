import pytest
from main import *
from util import *


@RevaTest(points=10, tier=0)
def test_add():
    assert add(3,4) == 7
    assert add(-10, 20) == 10
    
@RevaTest(points=10, tier=0)
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 5) == -3


