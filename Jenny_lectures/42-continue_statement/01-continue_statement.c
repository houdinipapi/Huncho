#include <stdio.h>

/**
  * main - uses continue statement
  */

void main(void)
{
	int a, i, sum = 0;

	for (i = 1; i <= 5; ++i)
	{
		printf("Enter a number:\n");
		scanf("%d", &a);

		if (a < 0)
		{
			continue;
		}
		sum = sum + a;
	}
	printf("Sum = %d\n", sum);
}
