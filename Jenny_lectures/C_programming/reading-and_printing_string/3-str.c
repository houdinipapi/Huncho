#include <stdio.h>

/**
 * main - reading and printing strings
 */

void main(void)
{
	char fname[30];
	char lname[30];

	printf("Enter your name: ");
	scanf("%s %s", fname, lname);

	printf("%s %s\n", fname, lname);
}
