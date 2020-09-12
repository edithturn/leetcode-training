def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	num = 0
	flag = "false"

	if x >= 2**31-1 or x <= -2**31: return 0
	if (x < 0):
		flag = "true"
		x = x*(-1)
	while (x > 0):
		a	=  x % 10
		num = num*10 + a
		x = x//10
	if num >= 2**31-1 or num <= -2**31: return 0
	if (flag == "true"):
		num = num*(-1)
	return (num)
num = 1534236469
print (reverse(num))