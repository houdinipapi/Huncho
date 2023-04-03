#include <stdio.h>

/**
 * main - reading and printing strings
 */

void main(void)
{
	char name[30];

	printf("Enter your name: ");
	scanf("%s", name);

	printf("%s\n", name);
}
