/* checking vowels */
#include <stdio.h>

void main(void)
{
	char ch;

	printf("Enter a character:\n");
	scanf("%c", &ch);

	switch (ch)
	{
		case 'a':
		case 'e':
		case 'o':
		case 'i':
		case 'u':
		printf("%c is a VOWEL\n", ch);
		break;

		default:
		printf("%c is NOT a vowel!!\n", ch);
	}
}
