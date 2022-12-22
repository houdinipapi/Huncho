#include <stdio.h>
#include <math.h>

/**
  * main - checks for a prime number
  */

void main(void)
{
	int i, j, n;

	printf("Enter a number:\n");
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
	{
		for (j = 2; j <= (i / j); j++)
		{
			if (!(i % j))
			{
				break;
			}
		}
			if (j > (i / j))
				printf("%d is a prime number\n", i);
	}
}
