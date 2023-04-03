#include <stdio.h>
#include <string.h>

/**
 * main - string concatenation without a predefined function
 */

void main(void)
{
	char first_name[30];
	char second_name[15];
	int len1, len2, i;

	printf("Enter your first and second name:\n");
	gets(first_name);
	gets(second_name);

	len1 = strlen(first_name);
	len2 = strlen(second_name);

	printf("%d\n", len1);
	printf("%d\n", len2);

	for (i = 0; i <= len2; i++)
	{
		first_name[len1 + i] = second_name[i];
	}
	printf("%s\n", first_name);
}
