#include <stdio.h>

/**
  * main - prints all possible combinations
  * of two two-digit numbers.
  */

void main(void)
{
	int i, j;

	for (i = 0; i < 100; ++i)
	{
		for (j = 1; j < 100; ++j)
		{
			if (j > i)
			{
				putchar((i / 10) + '0');
				putchar((i % 10) + '0');
				putchar(' ');
				putchar((j / 10) + '0');
				putchar((j % 10) + '0');

				if (i != 98)
				{
					putchar(',');
					putchar(' ');
				}
			}
		}
	}
	putchar('\n');
}
