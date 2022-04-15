from simple_library_01.functions import get_month_days


def test_get_month_days():
        assert 30 == get_month_days(1930, 12)
        assert 30 == get_month_days(1930, 2)
        assert 29 == get_month_days(1956, 2)
        assert 28 == get_month_days(1957, 2)
        assert 30 == get_month_days(2001, 4)
        assert 31 == get_month_days(2019, 5)
        try:
                a = get_month_days(2001, 14)
        except Exception as error:
                assert isinstance(error, AttributeError)
