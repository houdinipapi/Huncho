#include <stdio.h>

/**
  * main - prints remaining alphabets
  */

void main(void)
{
	char n, i;

	printf("Enter an alphabet:\n");
	scanf("%c", &n);

	for (i = n; i <= 'z'; i++)
	{
		printf("%c ", i);
	}
	printf("\n");
		//if (n == 'z')
		{
			for (i = n; i >= 'a'; i--)
			{
				printf("%c ", i);
			}
			printf("\n");
		}
}
