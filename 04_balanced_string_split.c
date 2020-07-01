#include <stdio.h>
#include <stdio.h>
#include <string.h>
/*
**Balanced strings are those who have equal quantity of 'L' and 'R' characters.
**Given a balanced string s split it in the maximum amount of balanced strings.
**Return the maximum amount of splitted balanced strings.
**Example 1:
**Input: s = "RLRRLLRLRL"
**Output: 4
**Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
**Example 2:
**Input: s = "RLLLLRRRLR"
**Output: 3
**Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
**Example 4:
**Input: s = "RLRRRLLRLL"
**Output: 2
**Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
*/

int balancedStringSplit(char * s)
{
	int cl;
	int total;
	int i;
	int c;

	c = 1;
	cl = 0;
	total = 0;
	i = 0;
	while(s[i] != '\0')
	{
		while(s[i + 1] != '\0' && s[i] == s[i + 1])
		{
			c = c + 1;
			i++;
		}
		cl = c;
		c = 1;
		i++;
		while(i <= strlen(&s[i]) && s[i] == s[i + 1])
		{
			if (cl == c)
			{
				cl = 0;
				c = 1;
				total = total + 1;
			}
			c = c + 1;
			i++;
		}
		if (cl == c)
		{
			cl = 0;
			c = 1;
			total = total + 1;
		}
		i++;
	}
	return (total);
}
int main()
{
	int r;
	char *str;

	str = "RLLLLRRRLR";
	r = balancedStringSplit(str);
	printf("%d", r);
	return (0);
}