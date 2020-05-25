#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define val 22

int is_point(char p){return (p=='.');}

char * defangIPaddr(char * address)
{
	int i;
	int j;
	char * cpy;

	cpy = malloc(val);

	if (strlen(address) > val)
	{
		return NULL;
		exit;
	}
	j = 0;
	while(*address)
	{
		if (is_point(*address))
		{
			cpy[j] =  '[';
			cpy[j + 1] = *address;
			cpy[j + 2] = ']';
			j = j+3;
		}
		else
		{
			cpy[j] = *address;
			j++;
		}
		
		address++;
	}
	cpy[j] = '\0';
	return cpy;
}

int main(){

char * str = "100.100.100.145";
char * new_str;

new_str = defangIPaddr(str);
printf("%s", new_str);
return (0);
}