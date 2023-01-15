#include <stdio.h>

/**
 * main - prints a mirrored staircase pattern
 */

void main(void)
{
	int i, j, n;

	/* Taking no. of rows */
	printf("Enter no. of rows: \n");
	scanf("%d", &n);

	/* Printing the Space and Pattern */
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= n; j++)
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
