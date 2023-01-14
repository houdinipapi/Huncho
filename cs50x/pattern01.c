#include <stdio.h>

/**
 * main - prints a pattern
 */

void main(void)
{
	int n, i, j;

	/* ASK FOR INPUT */
	printf("Enter a number: ");
	scanf("%d", &n);

	/* PRINT THE PATTERN */
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= i; j++)
		{
			printf("#");
		}
		printf("\n");
	}
}
