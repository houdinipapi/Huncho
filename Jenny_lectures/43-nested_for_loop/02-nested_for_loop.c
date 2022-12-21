#include <stdio.h>

/**
  * main - prints pattern of numbers
  */

void main(void)
{
	int i, j, n;

	printf("Enter number of columns:\n");
	scanf("%d", &n);

	for (j = 1; j <= n; ++j)
	{
		for (i = 9; i >= 0; --i)
		{
			printf("%d ", i);
		}
		putchar('\n');
	}
}
