# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
	if n > 21:
		return 2*(n  - 21)
	else:
		return -1*(n  - 21)

# Unit Test
def test_diff21():
	assert diff21(19) == 2
	assert diff21(10) == 11
	assert diff21(21) == 0

if __name__ == "__main__":
    test_diff21()
    print("OK")