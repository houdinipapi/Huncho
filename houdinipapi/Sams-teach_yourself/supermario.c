#include <stdio.h>

/**
 * main - prints an inverted right aligned pattern
 */

void main(void)
{
	int i, j, n;

	do {
		printf("No. of rows: ");
		scanf("%d", &n);
	} while(n < 1 || n > 9);

	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= (n - i); j++)
		{
			printf(".");
		}
		for (j = 1; j <= i; j++)
		{
			printf("#");
		}
		printf("\n");
	}
}
