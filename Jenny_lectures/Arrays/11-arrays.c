#include <stdio.h>

/**
  * main - prints before and after alphabets
  */

void main(void)
{
	char n, i;

	printf("Enter an alphabet:\n");
	scanf("%c", &n);

	printf("These are the alphabets that are after %c:\n", n);
	for (i = (n + 1); i <= 'z'; i++)
	{
		printf("%c ", i);
	}
	printf("\n");


	printf("These are the alphabets that are before %c:\n", n);
			for (i = (n - 1); i >= 'a'; i--)
			{
				printf("%c ", i);
			}
			printf("\n");
}
