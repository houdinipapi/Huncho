#include "main.h"
#include <stdio.h>

/**
  * main - checks if the character is lowercase
  * Return: Success
  */

int main(void)
{
	char i, j;

	printf("Enter a character:\n");
	scanf("%c", &i);

	j = _islower(i);
	_putchar(j + '0');

	printf("\n");

	return (0);
}
