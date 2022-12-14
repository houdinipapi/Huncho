#include <stdio.h>

/**
  * main - prints multiplication table
  */

void main(void)
{
	int i, factor, n;

	printf("Enter a number to print multiplication table:\n");
	scanf("%d", &n);
	printf("Enter the multiiplication factor:\n");
	scanf("%d", &factor);

	/* Multiplication Table */
	printf("_______________________________\n");

	for (i = 1; i <= factor; i++)
	{
		printf("%d X %d = %d\n", n, i, n * i);
	}
}
