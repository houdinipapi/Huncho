#include <stdio.h>

/**
   * main - prints a pattern
   */

void main(void)
{
	int i = 1, j;

	while (i < 7)
	{
		j = i;
		while (j < 7)
		{
			printf("* ");
			j++;
		}
		putchar('\n');
		i++;
	}
}
