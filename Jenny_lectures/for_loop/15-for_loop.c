#include <stdio.h>

/**
  * main - prints the sum of all even numbers
  * between 1 and j
  */

void main(void)
{
	int i, j, k;

	k = 0;

	printf("Enter a number:\n");
	scanf("%d", &j);

	for (i = 1; i <= j; i++)
	{
		if (i % 2 == 0)
		{
			k = k + i;
		}
	}
	printf("Sum of all even numbers between 1 and %d is: %d\n", j, k);
}
