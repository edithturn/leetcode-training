#include <stdio.h>
#include <stdlib.h>

int is_vowal(char s)
{
    if (s == 'a' || s == 'e' || s == 'i' || s == 'o' || s == 'u')
        return 1;
    else if (s == 'A' || s == 'E' || s == 'I' || s == 'O' || s == 'U')
        return 1;
    else
        return 0;
}
char *removeVowels(char *S)
{    
    char *v = "aeiou";
    char *pdest;
	char letter;
	int i;

	i = 0;
    pdest = (char *)malloc(1);
	int len = 1;
    if (pdest == NULL)
        return (NULL);
	int offset = 0;
   
   while(*S)
   {
	   letter = *S;
        if (!(is_vowal(letter)))
        {
			pdest = (char *)realloc(pdest, len + 1);
			len++;
			*(pdest + offset) = letter;
			offset++;
        }
       S++;
   }

   *(pdest + offset) = '\0';
    return pdest;
}
int main()
{
	char *S = "leetcodeisacommunityforcoders";
	char *R;

	R = removeVowels(S);
	printf("%s", R);
	return (0);
}