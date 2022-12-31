#include <stdio.h>

/**
  * main - prints a pattern
  */

void main(void)
{
	int i = 0, j;

	printf("Printing a pattern\n");

	while (i < 7)
	{
		j = 1;
		while (j < 7)
		{
			printf("%d ", j);
			j++;
		}
		putchar('\n');
		i++;
	}
}
