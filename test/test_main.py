import main


def test_add():
    assert main.add(3, 4) == 7
    assert main.add(3.5, 4) == 7


def test_subract():
    assert main.subtract(8, 3) == 5
    assert main.subtract(4, 2) == 2
