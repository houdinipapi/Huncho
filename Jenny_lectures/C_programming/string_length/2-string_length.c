#include <stdio.h>

/**
 * main - calculates length of a string
 * using while loop
 */

void main(void)
{
	int i = 0;
	int count = 0;
	char name[30];

	printf("Enter your Name: ");
	gets(name);

	while (name[i] != '\0')
	{
		count++;
		i++;
	}
	printf("Length of the string is %d\n", count);
}
