#include <stdio.h>

/**
  * main - function that prints truangle pyramid
  * pattern using *
  */

void main(void)
{
	int i, j, rows;

	printf("Eter the number of rows:\n");
	scanf("%d", &rows);

	for (i = 1; i <= rows; i++)
	{
		/* prints one row of triangle */
		for (j = 1; j <= i; j++)
		{
			printf("* ");
		}
		putchar('\n');
	}
}
