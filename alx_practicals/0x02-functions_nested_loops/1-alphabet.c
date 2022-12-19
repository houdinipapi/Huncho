#include "main.h"
/**
  * print_alphabet - prints the alphabet in lowercase
  * followed by a new line
  * only use _putchar twice in the code
  */

void print_alphabet(void)
{
	char ch;

	for (ch = 'a'; ch <= 'z'; ++ch)
	{
		_putchar(ch);
	}
	_putchar('\n');
}
