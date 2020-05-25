#include <stdio.h>
#include <stdlib.h>

int is_point(char p)
{
	if (p == '.')
		return (1);
	else
		return (0);
}

char * defangIPaddr(char * address)
{
	int i;
	int j;
	char * cpy;
	cpy = malloc(24);

	i = 0;
	j = 0;
	while(address[i])
	{
		if (is_point(address[i]))
		{
			cpy[j] =  '[';
			cpy[j + 1] = address[i];
			cpy[j + 2] = ']';
			j = j+3;
		
		}
		else
		{
			cpy[j] = address[i];
			j++;
		}
		
		i++;
	}
	cpy[j] = '\0';
	return cpy;
}

int main(){

char * str = "1.1.1.1";
char * new_str;

new_str = defangIPaddr(str);
printf("%s", new_str);
return (0);
}