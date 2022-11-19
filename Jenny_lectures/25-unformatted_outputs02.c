#include <stdio.h>

int main(void)
{
	char ch;

	printf("Input a character: \n");
	ch = getc(stdin);
	printf("The character is: %c\n", ch);
	return (0);
}
