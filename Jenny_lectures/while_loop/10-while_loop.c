#include <stdio.h>

/**
  * main - prints a pattern
  */

void main(void)
{
	int i = 1, j;

	printf("Printing a pattern\n");

	while (i <= 7)
	{
		j = 7;
		while (j >= i)
		{
			printf("%d ", j);
			j--;
		}
		putchar('\n');
		i++;
	}
}
