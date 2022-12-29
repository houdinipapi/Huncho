#include <stdio.h>
/**
  * main - prints lowercase or uppercase
  */

void main(void)
{
	char c;

	printf("Type in l or u:\n");
	scanf("%c", &c);

	if (c == 'l' || c == 'u')
	{
		for (c = 'a'; c <= 'z'; c++)
			printf("%c ", c);
	}
	else if (c == 'L' || c == 'U')
	{
		for (c = 'A'; c <= 'Z'; c++)
		{
			printf("%c ", c);
		}
	}
	printf("\n");
}
