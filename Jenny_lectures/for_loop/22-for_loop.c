#include <stdio.h>

/**
  * main - print even numbers within the given parameter
  */

void main(void)
{
	int i, n;

	printf("Enter the parameter:\n");
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
	{
		if (i % 2 == 0)
			printf("%d ", i);
	}
	putchar('\n');
}
