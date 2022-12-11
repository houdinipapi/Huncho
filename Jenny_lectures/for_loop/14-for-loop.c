#include <stdio.h>

/**
  * main - prints odd numbers using for loop
  */

void main(void)
{
	int i = 1;

	for (; i <= 100; i++)
	{
		if (i % 2 != 0)
		{
			printf("%d, ", i);
		}
	}
	putchar('\n');
}
