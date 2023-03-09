#include <stdio.h>
#include <string.h>

/**
 * main - converts lowercase into uppercase
 */

void main(void)
{
	int i, str_len;
	char str[30];

	printf("Enter a name or word in lowercase: ");
	gets(str);

	for (i = 0; i != '\0'; i++)
	{
		if (i >= 'a' && i <= 'z')
		{
			str[i] += 32;
		}
