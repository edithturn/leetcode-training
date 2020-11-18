# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
	if (0 < hour < 7 or 20 < hour < 24) and talking == True:
		return True
	else:
		return False

# Unit Test
def test_parrot_trouble():
	assert parrot_trouble(True, 6) == True
	assert parrot_trouble(True, 7) == False
	assert parrot_trouble(False, 6) == False

if __name__ == "__main__":
    test_parrot_trouble()
    print("OK")