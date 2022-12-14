#include <stdio.h>

/**
  * main - prints multiplication table
  * using while loop
  */

void main(void)
{
	int i, factor, n;

	printf("Enter a multiplication factor:\n");
	scanf("%d", &factor);

	printf("Enter the number of terms in table:\n");
	scanf("%d", &n);

	putchar('\n');

	for (i = 1; i <= n; i++)
	{
		printf("%d X %d = %d\n", factor, i, factor * i);
	}
}
