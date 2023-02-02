#include <stdio.h>

/**
 * main - reading and printing strings
 */

void main(void)
{
	char name[30];

	printf("Enter your name: ");
	gets(name);

	printf("%s\n", name);
	printf("%s\n", &name);
}
