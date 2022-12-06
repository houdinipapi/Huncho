#include <stdio.h>

/**
  * main - prints alphabetical letters in reverse form
  */

void main(void)
{
	char i;

	for (i = 'Z'; i >= 'A'; i--)
	{
		printf("%c\n", i);
	}
}
