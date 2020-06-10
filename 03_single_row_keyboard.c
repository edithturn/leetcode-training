#include <stdio.h>
/*
**There is a special keyboard with all keys in a single row.
**Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.
**You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
**Example 1:
**Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
**Output: 4
**Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
**Total time = 2 + 1 + 1 = 4. 
**Example 2:
**Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
**Output: 73
*/
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
