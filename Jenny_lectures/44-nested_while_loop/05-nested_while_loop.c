#include <stdio.h>

/**
  * main - prints an inverted pattern
  */

void main(void)
{
	int i = 1, j;

	while (i <= 7)
	{
		j = 7;
		while (j >= i)
		{
			printf("* ");
			j--;
		}
		putchar('\n');
		i++;
	}
}
