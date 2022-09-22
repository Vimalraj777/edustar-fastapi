import pytest
from app.calculations import add


@pytest.mark.parametrize("num1,num2,expected",[
    (3,4,7),(5,6,11),(5,4,9)
    ])
def test_Add(num1,num2,expected):
    assert add(num1,num2)==expected


def test_add():
    sum=add(5,3)
    assert sum==8

