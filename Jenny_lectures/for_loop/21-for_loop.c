#include <stdio.h>

/**
  * main - prints inverted pyramid
  */

void main(void)
{
	int row, space, rows, star;

	star = 0;

	printf("Enter the number of rows in a reverse pyramid:\n");
	scanf("%d", &rows);

	for (row = rows; row >= 1; row--)
	{
		/* Printing spaces */
		for (space = 0; space <= rows - row; space++)
		{
		printf(" ");
		}

		/* Printing Stars */
		star = 0;
		while (star != (2 * row - 1))
		{
			printf("* ");
			star++;
		}
		printf("\n");
	}
}
