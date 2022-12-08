#include <stdio.h>

/**
  * main - a program that prints the alphabet in lowercase
  * followed by a new line
  * only use putchar function & use it only twice
  */

void main(void)
{
	char ch;

	ch = 'a';

	while (ch <= 'z')
	{
		putchar(ch);
		ch++;
	}
	putchar('\n');
}
