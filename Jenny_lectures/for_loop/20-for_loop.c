#include <stdio.h>

/**
  * main - prints a pyramid using for loop
  */

void main(void)
{
	int row, space, rows, star = 0;

	printf("Enter the number of rows in a pyramid:\n");
	scanf("%d", &rows);

	for (row = 1; row <= rows; row++)
	{
		/* Printing spaces */
		for (space = 1; space <= rows - row; space++)
		{
			printf(" ");
		}
		/* Printing stars */
		while (star != (2 * row - 1))
		{
			printf("* ");
			star++;
		}
		star = 0;
		putchar('\n');
	}
}
