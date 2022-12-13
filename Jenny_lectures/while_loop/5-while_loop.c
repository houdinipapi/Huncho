#include <stdio.h>

/**
  * main - function that prints alphabets
  * omitting 'g' and 's'
  */

void main(void)
{
	char ch;

	ch = 'a';

	while (ch <= 'z')
	{
		if (ch != 'g' && ch != 's')
			printf("%c ", ch);
		ch++;
	}
	putchar('\n');
}
