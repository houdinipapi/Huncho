#include "main.h"

/**
  * print_alphabet_x10 - prints the alphabet 10 times
  * followed by a new line
  * use _putchar only twice
  */

void print_alphabet_x10(void)
{
	char b, c;

	for (c = 1; c <= 10; ++c)
	{
		for (b = 'a'; b <= 'z'; ++b)
		{
			_putchar(b);
		}
		_putchar('\n');
	}
}
