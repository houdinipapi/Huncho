#include <stdio.h>

/**
  * main - prints single numbers of base 10
  * followed by a new line
  */

void main(void)
{
	int i = 0;

	while (i < 10)
	{
		printf("%d", i);
		i++;
	}
	putchar('\n');
}
