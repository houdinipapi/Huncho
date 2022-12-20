#include <stdio.h>

/**
  * main - checks for lowercase letters
  * Return: 1 if lowercase, 0 if not
  */

int main(void)
{
	char i;

	printf("Enter an alphabet:\n");
	scanf("%c", &i);

	if (i >= 'a' && i <= 'z')
		putchar('1');

	else
		putchar('0');

	putchar('\n');
}
