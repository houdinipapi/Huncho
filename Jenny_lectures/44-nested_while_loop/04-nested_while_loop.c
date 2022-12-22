#include <stdio.h>

/**
  * main - print a pattern of stars
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
