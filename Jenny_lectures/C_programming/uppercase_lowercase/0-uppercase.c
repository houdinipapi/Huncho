#include <stdio.h>
#include <string.h>

/**
 * main - change uppercase into lowercase
 */

void main(void)
{
	int i;
	char str[30];

	printf("Enter a name with mixed uppercase & lowercase letters: ");
	gets(str);

	if (str[i] >= 'A' && str[i] <= 'Z')
	{
		str[i] += 32;
	}
	printf("%s\n", str);
}
