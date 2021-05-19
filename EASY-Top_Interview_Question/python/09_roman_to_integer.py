# Roman to Integer

def convert_integer(roman : str):
	total = 0
	i = 0
	value = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "M" : 1000}
	while i  < len(roman):
		if i + 1 < len(roman) and value[roman[i]] < value[roman[i + 1]] :
			total = total + (value[roman[i + 1]] - value[roman[i]] )
			i = i + 2
		else:
			total = total + value[roman[i]]
			i = i + 1
	return total

print(convert_integer("XXXVI"))