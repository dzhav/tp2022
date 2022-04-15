from simple_library_01.functions import is_leap


def test_is_leap():
	assert False == is_leap(2022)
	assert False == is_leap(2021)
	assert True == is_leap(2020)
	assert False == is_leap(1900)
	assert True == is_leap(2000)
	try:
		am = is_leap(-2)
	except Exception as error:
		assert isinstance(error, AttributeError)

