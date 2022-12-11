#include <stdio.h>

/**
  * main - prints even numbers using while loop
  */

void main(void)
{
	int i = 2;

	while (i <= 100)
	{
		printf("%d, ", i);
		i = i + 2;
	}
	putchar('\n');
}
