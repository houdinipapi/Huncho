#include <stdio.h>

/**
 * main - prints a right-aligned pyramid
 */

void main(void)
{
	int i, j, n;

	/* Asks for no. of rows */
	printf("Enter the no. of rows: \n");
	scanf("%d", &n);

	/* printing the output */
	for (i = 1; i <= n; i++)
	{
		/* printing spaces */
		for (j = 1; j <= (n - i); j++)
		{
			printf(" ");
		}

		/* printing pattern */
		for (j = 1; j <= i; j++)
		{
			printf("#");
		}

		printf("..");
		printf("\n");
	}
}
