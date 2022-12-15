#include <stdio.h>

/**
  * main - prints inverted triangular shape
  */

void main(void)
{
	int i, j, rows;

	printf("Enter the number of rows:\n");
	scanf("%d", &rows);

	for (i = rows; i > 0; i--)
	{
		for (j = i; j > 0; j--)
		{
			printf("* ");
		}
		putchar('\n');
	}
}
