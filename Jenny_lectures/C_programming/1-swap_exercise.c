#include <stdio.h>
#include <string.h>

/**
 * main - string reversal
 * Return: 0
 */

int main(void)
{
	int i, j, str_len;
	char ch, str_name[30];

	printf("Enter a name: ");
	gets(str_name);

	str_len = strlen(str_name);
	printf("%d\n", str_len);

	for (i = 0, j = (str_len - 1); i < (str_len - 1); i++, j--)
	{
		ch = str_name[i];
		str_name[i] = str_name[j];
		str_name[j] = ch;
	}
	printf("%s\n", str_name);

	return (0);
}
