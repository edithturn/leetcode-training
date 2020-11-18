#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

# Trouble if a_amile = True and b_smile = True
# Truoble if a_smile = False and b_smile = False

def money_trouble(a_smile, b_smile):
	if (a_smile and b_smile) or ( not a_smile  and not b_smile):
		return True
	else:
		return False

print (money_trouble(True, True))
print (money_trouble(False, False))
print (money_trouble(True, False))