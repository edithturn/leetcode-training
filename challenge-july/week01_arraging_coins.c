#include <stdio.h>

int arrangeCoins(int n)
{
	unsigned int count;
	unsigned int sum;

	count = 0;
	sum = 0;

	while (sum <= n)
	{
		count = count + 1;
		sum = sum + count;
	}
	return (count - 1);
}
int main()
{
	int t_row_coins;
	t_row_coins =	arrangeCoins(5);
	printf("%d\n", t_row_coins);
	return t_row_coins;
}