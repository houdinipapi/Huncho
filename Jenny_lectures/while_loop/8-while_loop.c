#include <stdio.h>

/**
  * main - print even numbers using while loop
  */

void main(void)
{
	int i = 1, n;

	printf("Enter the parameter:\n");
	scanf("%d", &n);

	while (i <= n)
	{
		i++;
		if (i % 2 == 0)
			printf("%d ", i);
	}
	putchar('\n');
}
