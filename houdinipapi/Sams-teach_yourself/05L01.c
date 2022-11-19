#include <stdio.h>

/**
  *main - entry point
  *Return: success (0)
  */

int main(void)
{
	int ch;

	printf("Please type in one character:\n");
	ch = getc(stdin);
	printf("The character you just entered is: %c\n", ch);
	return (0);
}
