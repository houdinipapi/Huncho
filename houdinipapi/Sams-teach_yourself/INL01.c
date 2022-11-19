#include <stdio.h>

/**
  *main - main function
  *Description: Read input by calling getc()
  *Return: success
  */

int main(void)
{
	int ch;

	printf("Please type in one character:\n");
	ch = getc(stdin);
	printf("The character you just entered is: %c\n", ch);
	return (0);
}
