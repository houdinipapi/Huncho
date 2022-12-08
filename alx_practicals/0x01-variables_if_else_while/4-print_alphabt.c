#include <stdio.h>

/**
  * main - prints all the alphabet in lowercase,
  * followed by a new line
  * Use only putchar twice
  */

void main(void)
{
	char ch;

	ch = 'a';

	while (ch <= 'z')
	{
		if (ch != 'q' && ch != 'e')
			putchar(ch);
			ch++;
	}
	putchar('\n');
}
