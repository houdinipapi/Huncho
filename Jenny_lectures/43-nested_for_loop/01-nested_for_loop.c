#include <stdio.h>

/**
  * main - prints a pattern
  */

void main(void)
{
	int i, j;

	for (j = 1; j <= 10; ++j)
	{
		for (i = 1; i <= 5; ++i)
		{
			printf("* ");
		}
	putchar('\n');
	}
}
