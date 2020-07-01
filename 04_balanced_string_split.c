#include <stdio.h>


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
		while(s[i] == s[i + 1])
		{
			c = c + 1;
			i++;
		}
		cl = c;
		c = 1;
		i++;
		while(s[i] == s[i + 1])
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

	str = "RLRRRLLRLL";
	r = balancedStringSplit(str);
	printf("%d", r);
	return (0);
}