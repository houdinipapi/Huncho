#include <stdio.h>
#include <string.h>

/**
 * main - concatenates string
 */

void main(void)
{
	char first_name[30];
	char second_name[10];

	printf("Enter your first and second name:\n");
	scanf("%s %s", first_name, second_name);

	strcat(first_name, second_name);

	printf("%s\n", first_name);
}
