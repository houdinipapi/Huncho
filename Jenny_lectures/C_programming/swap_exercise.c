#include <stdio.h>
#include <string.h>

/**
 * main - reverse a string
 * Return - Always 0
 */

int main(void)
{
	int i, str_len;
	char str[30], ch;

	printf("Enter your name: ");
	gets(str);

	str_len = strlen(str);
	printf("%d\n", str_len);

	for (i = 0; i < (str_len / 2); i++)
	{
		ch = str[i];
		str[i] = str[str_len - 1 - i];
		str[str_len - 1 - i] = ch;
	}

	printf("%s\n", str);

	return (0);
}
