#include <stdio.h>

/**
 * main - reading and printing strings
 */

void main(void)
{
	char name[30];

	printf("Enter your name: ");
	gets(name);

	printf("%.5s\n", name);
	printf("%10.5s\n", &name[2]);
}
