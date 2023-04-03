#include <stdio.h>
#include <string.h>

/**
 * main - string reversal
 */

void main(void)
{
	int j, i, name_len;
	char name[30], ch;

	printf("Enter your name: ");
	gets(name);

	name_len = strlen(name);

	for (i = 0, j = (name_len - 1); i < (name_len / 2); i++, j--)
	{
		ch = name[i];
		name[i] = name[j];
		name[j] = ch;
	}
	printf("%s\n", name);
}
