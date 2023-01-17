#include <stdio.h>

/**
 * main - prints a mario pattern
 */

void main(void)
{
	int n, i, j;

	do
	{
		printf("Enter a number of rows: \n");
		scanf("%d", &n);
	}
	while (n < 1 || n > 9);

	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= (n - i); j++)
		{
			printf(" ");
		}
		for (j = 1; j <= i; j++)
		{
			printf("#");
		}
		printf("\n");
	}
}
