#include <stdio.h>

/**
  * main - functio that prints even numbers
  * between 1 and 100
  */

void main(void)
{
	int i;

	for (i = 1; i <= 100; i++)
	{
		if (i % 2 == 0)
		{
			printf("%d, ", i);
		}
	}
	putchar('\n');
}
