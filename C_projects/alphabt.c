#include <stdio.h>

/**
 * main - print alphabets apart from "e"
 */

void main(void)
{
	char i;

	for (i = 'a'; i >= 'a'; i++)
	{
		if (i != 'e' && i <= 'z')
		{
			printf("%c \n", i);
		}
	}
}
