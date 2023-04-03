#include <stdio.h>
#include <string.h>

/**
 * main - concatenating string
 */

void main(void)
{
	char first_name[30];
	char second_name[15];
	int first_length;
	int second_length;
	int i;

	printf("Enter your first name: ");
	gets(first_name);
	printf("Enter your second name: ");
	gets(second_name);

	first_length = strlen(first_name);
	second_length = strlen(second_name);

	for (i = 0; i <= second_length; i++)
	{
		first_name[first_length + i] = second_name[i];
	}
	printf("The new string is: %s\n", first_name);
}
