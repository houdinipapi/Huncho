#include <stdio.h>
#include <string.h>

/**
 * main - string reversal
 * Return: 0
 */

int main(void)
{
	char s1[30];

	printf("Enter your name: ");
	gets(s1);

	strrev(s1);

	printf("%s\n", s1);

	return(0);
}
