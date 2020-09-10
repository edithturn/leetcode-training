class Solution:
	def fizzBuzz(self, n):
		x = 1
		li = list()
		while x <= n:
			if((x % 3 == 0) and (x % 5 == 0)):
				li.append('FizzBuzz')
			elif(x % 5 == 0):
				li.append('Buzz')
			elif(x % 3 == 0):
				li.append('Fizz')
			else:
				li.append(str(x))
			x = x + 1
		return li

if __name__ == "__main__":
	fb = Solution()
	print (fb.fizzBuzz(15))