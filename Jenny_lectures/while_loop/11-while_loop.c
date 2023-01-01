#include <stdio.h>

/**
   * main - prints a pattern
   */

void main(void)
{
	int i = 1, j = 1;

	while (i < 7)
	{
		while (j < 7)
		{
			printf("* ");
			j++;
		}
		putchar('\n');
		i++;
	}
}
