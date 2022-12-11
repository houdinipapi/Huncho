#include <stdio.h>

/**
  * main - prints odd numbers between 1 and 100
  */

void main(void)
{
	int i = 1;

	while (i <= 100)
	{
		printf("%d ,", i);
		i = i + 2;
	}
	putchar('\n');
}
