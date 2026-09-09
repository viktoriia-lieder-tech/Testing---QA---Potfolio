import pytest
from unittest import mock

from main import add, devide, play_random, ProductionClass, print_me, is_not_flat, sum_list
@pytest.mark.parametrize('input1, input2, expected, [(1, 4, 5), (5, 3, 8)]')
def test_add(input1, input2, expected):
    result = add(input1, input2)
    assert result == expected

def test_devide():
    result = devide(8, 2)
    assert result == 4
    with pytest.raises(ZeroDivisionError):
        10 / 0

@mock.patch('main.randint', return_value=7)
def test_play_random(mocked_randint):
    result = play_random()
    assert result == "größer"


def test_productionclass():
    instanz = ProductionClass()
    instanz.somethimg = mock.MagicMock()
    instanz.method()
    instanz.something.assert_called_once_with(1, 2, 3)

def test_print_me(capsys):
    print_me()
    captures = capsys.readouter()
    assert captures.out == "hallo\n"    

def test_is_not_flat(my_data):
    assert is_not_flat(my_data) == false

def test_sum_list(my_data):
    assert sum_list(my_data) == 10

test_sum_list()   