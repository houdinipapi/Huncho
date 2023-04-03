#include <stdio.h>
#include <string.h>

/**
 * main - concatenating strings
 */

void main(void)
{
	char f_name[30];
	char s_name[15];

	printf("Enter your first name: ");
	gets(f_name);
	printf("Enter your second name: ");
	gets(s_name);

	strncat(f_name, s_name, 4);
	printf("The new string is: %s\n", f_name);
}
