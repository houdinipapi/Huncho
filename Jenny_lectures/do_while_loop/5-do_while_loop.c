#include <stdio.h>

/**
  * main - prints even numbers using do while loop
  * within a user's specified parameter
  */

void main(void)
{
	int i = 1, n;

	printf("Enter a parameter:\n");
	scanf("%d", &n);

	do {
		if (i % 2 == 0)
		{
			printf("%d ", i);
		}
		i++;
	} while (i <= n);

	putchar('\n');
}
