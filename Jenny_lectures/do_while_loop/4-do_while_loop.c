#include <stdio.h>

/**
  * main - prints multiplication table
  * using do while loop
  */

void main(void)
{
	int i, factor, n;

	i = 1;

	printf("Enter a constant number:\n");
	scanf("%d", &factor);

	printf("Enter the number of times:\n");
	scanf("%d", &n);

	putchar('\n');

	do {
		printf("%d X %d = %d\n", factor, i, factor * i);
		i++;
	} while (i <= n);
}
