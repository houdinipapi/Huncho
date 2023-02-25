#include <stdio.h>
#include <string.h>

/**
 * main - string concatenation
 */

void main(void)
{
	char first_name[30];
	char second_name[15];

	printf("Enter your first and second name:\n");
	scanf("%s %s", first_name, second_name);

	strncat(first_name, second_name, 3);

	printf("%s\n", first_name);
}
