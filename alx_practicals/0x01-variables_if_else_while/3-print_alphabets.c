#include <stdio.h>

/**
  * main - prints the alphabet in lowercase
  * and then in uppercase, followed by a new line
  * Only use putchar function & 3 times maximum
  */

void main(void)
{
	char ch;

	for (ch = 'a'; ch <= 'z'; ch++)
	{
		putchar(ch);
	}

	for (ch = 'A'; ch <= 'Z'; ch++)
	{
		putchar(ch);
	}

	putchar('\n');
}
