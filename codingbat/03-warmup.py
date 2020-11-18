# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

import unittest

def sum_double(a, b):
	if a == b:
		sum = 2*(a + b)
	else:
		sum = a + b
	return sum

# Unit Test
def test_sum():
	assert sum_double(1, 2) == 3
	assert sum_double(3, 2) == 5
	assert sum_double(2, 2) == 8

if __name__ == "__main__":
    test_sum()
    print("OK")