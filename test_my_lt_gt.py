from math import e, pi

from my_lt_gt import my_lt

def test_my_lt():
	assert my_lt(e, pi)

def test_my_lt_2():
	assert my_lt(pi, e)
