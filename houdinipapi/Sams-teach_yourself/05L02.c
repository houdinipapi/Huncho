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
	printf("The numeric value of the character you just entered is: %d\n", ch);
	return (0);
}
