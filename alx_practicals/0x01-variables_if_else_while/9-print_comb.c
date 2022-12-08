#include <stdio.h>

/**
  * main - prints all the possible combinations of single numbers
  * ascending order
  * only use putchar (four times)
  */

void main(void)
{
	int i;

	for (i = '0'; i <= '9'; i++)
	{
		putchar(i);

		if (i != '9')
		{
			putchar(',');
			putchar(' ');
		}
	}
	putchar('\n');
}
