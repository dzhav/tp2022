from simple_library_01.functions import add


def test_add():
        assert 4 == add(2,2)
        assert 25 == add(10,15)
        assert 5 == add(1,4)
        assert 2021 == add(1001, 1020)
        assert 2500 == add(150, 2350)
