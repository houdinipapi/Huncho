#include <stdio.h>

/**
 * main - printing and accessing arrays
 */

void main(void)
{
	char name[15];

	printf("Enter your name: ");
	scanf("%s", name);

	printf("The 3rd letter of your name is %s.\n", name[2]);
}
