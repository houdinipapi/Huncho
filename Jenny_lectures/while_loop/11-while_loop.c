#include <stdio.h>

/**
   * main - prints a pattern
   */

void main(void)
{
	int i = 1, j;

	while (i <= 7)
	{
		j = 1;
		while (j <= i)
		{
			printf("* ");
			j++;
		}
		putchar('\n');
		i++;
	}
}
