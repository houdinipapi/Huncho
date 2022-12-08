#include <stdio.h>

/**
  * main - prints all single digit numbers of base 10
  * followed by a new line
  * only use putchar function (twice)
  */

void main(void)
{
	int i;

	for (i = '0'; i <= '9'; i++)
	{
		putchar(i);
	}
	putchar('\n');
}
