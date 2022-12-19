#include <stdio.h>

/**
  * main - prints 0-9 ten times
  */

void main(void)
{
	int i, j;

	for (i = 1; i <= 10; i++)
	{
		for (j = 0; j <= 9; j++)
		{
			printf("%d ", j);
		}
		printf("\n");
	}
}
