#include <stdio.h>

/**
  * main - function that prints the preceding vowels
  * using while loop
  */

void main(void)
{
	char i, ch;

	printf("Enter an alphabet:\n");
	scanf("%c", &ch);

	printf("The preceding alphabets are: ");

	i = ch;
	while (i >= 'a')
	{
		printf("%c ", i);
		i--;
	}
	putchar('\n');
}
