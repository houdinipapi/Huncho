#include <stdio.h>

int main(void)
{
	char ch[30];

	printf("Input a string of characters: \n");
	gets(ch);
	printf("The string is: %s\n", ch);
	return (0);
}
