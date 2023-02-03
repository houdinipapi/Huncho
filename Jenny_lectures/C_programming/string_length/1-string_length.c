#include <stdio.h>
#include <string.h>

/**
 * main - calculates length of a string
 */

void main(void)
{
	unsigned int count = 0;
	char name[30];

	printf("Enter your name: ");
	gets(name);

	count = strlen(name);
	printf("Length of string is: %d\n", count);
}
