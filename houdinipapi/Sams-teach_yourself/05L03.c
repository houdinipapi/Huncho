#include <stdio.h>

/**
  *main - entry point
  *Return: success (0)
  */

int main(void)
{
	int ch1, ch2;

	printf("Please type in two characters together:\n");
	ch1 = getchar();
	ch2 = getchar();
	printf("The first character you entered is: %c\n", ch1);
	printf("The second character you entered is: %c\n", ch2);
	return (0);
}
