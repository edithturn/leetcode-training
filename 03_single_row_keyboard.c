#include <stdio.h>

int return_index(char *keyboard, char c){
	int i;
	i = 0;
	while(keyboard[i])
	{
		if (keyboard[i] == c)
			return i;
		i++;
	}
	return 0;
}
int calculateTime(char *keyboard, char *word){
	int index;
	int i;
	int total;
	int sub_total;


	total = return_index(keyboard, word[0]);
	i = 1;
	while(word[i])
	{
		sub_total = (return_index(keyboard, word[i - 1])) - (return_index(keyboard, word[i]));
		if (sub_total < 0)
			sub_total = sub_total * (-1);
		total = total + sub_total;
		i++;
	}
	return total;
}

int main(){
	int time;
	char *word;
	char *keyboard;

	keyboard = "pqrstuvwxyzabcdefghijklmno";
	word = "leetcode";
	time = 0;
	time = calculateTime(keyboard, word);
	printf("%d\n", time);
	return (0);
}
