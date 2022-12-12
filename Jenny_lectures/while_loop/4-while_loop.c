#include <stdio.h>

/**
  * main - print natural numbers
  * in reverse using while loop
  */

void main(void)
{
	int i, j;


	printf("Enter a number:\n");
	scanf("%d", &j);
	printf("\nThe reverse order is: ");

	for (i = j; i >= 1; i--)
	{
		printf("%d, ", i);
	}
	putchar('\n');
}
