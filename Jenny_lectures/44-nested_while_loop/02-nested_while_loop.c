#include <stdio.h>

/**
  * main - prints numbers in reverse
  */

void main(void)
{
	int i = 0, j = 5;

	while (i <= 5)
	{
		while (j > 0)
		{
			printf("%d ", j--);
		}
		printf("%d ", i++);
	}
	putchar('\n');
}
