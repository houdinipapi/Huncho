#include <stdio.h>
#include <string.h>

/**
 * main - string concatenation without a predefined function
 */

void main(void)
{
	char first_name[30];
	char second_name[15];
	int l1;

	printf("Enter your first and second name:\n");
	scanf("%s %s", first_name, second_name);

	l1 = strlen(first_name);

	printf("%d\n", l1);
}
