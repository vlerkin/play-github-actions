from main import add_numbers


def test_add_2_3():
    assert add_numbers(2, 3) == 5


def test_add_2_3_4():
    assert add_numbers(2, 3, 4) == 9
