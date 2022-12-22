#include <stdio.h>
#include <math.h>

/**
  * main - checks for a composite number
  */

void main(void)
{
	int i, j, n;

	printf("Enter a number:\n");
	scanf("%d", &n);

	for (i = 2; i <= n; i++)
	{
		for (j = 2; j <= (i/j); j++)
		{
			if (i % j == 0)
			{
				printf("%d is composite\n", i);
				break;
			}
		}
	}
}
