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
	int r;
	int total;

	r = 0;
	total =0;
	for(int i = 0; i < strlen(s); i++)
	{
		if(s[i] == 'R')
		{
			total++;
		}else {
			total--;
		}
		if(total == 0)
		{
			r++;
		}
	}
		return r;
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