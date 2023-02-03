#include <stdio.h>
#include <string.h>

/**
 * main - concatenating a string
 */

void main(void)
{
	char first_name[30];
	char second_name[15];

	printf("Enter your first name: ");
	gets(first_name);
	printf("Enter your second name: ");
	gets(second_name);

	strcat(first_name, second_name);
	printf("The new name is: %s\n", first_name);
}
