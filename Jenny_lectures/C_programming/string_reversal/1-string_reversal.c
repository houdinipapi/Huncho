#include <stdio.h>
#include <string.h>

/**
 * main - string revrsal
 */

void main(void)
{
	char name[30], ch;
	int str_len, i;

	printf("Enter a string:");
	gets(name);

	str_len = strlen(name);
	printf("%d\n", str_len);

	for (i = 0; i < (str_len / 2); i++)
	{
		ch = name[i];
		name[i] = name[str_len - 1 - i];
		name[str_len - 1 - i] = ch;
	}
	printf("%s\n", name);
}
