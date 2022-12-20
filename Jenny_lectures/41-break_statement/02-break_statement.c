#include <stdio.h>

/**
  * main - print sum of numbers
  */

void main(void)
{
	int i, a, sum = 0;

	do {
		printf("Enter a number:\n");
		scanf("%d", &a);

		if (a < 0)
		{
			break;
		}
		sum = sum + a;
		i++;
	} while (1);
	{
	printf("Sum = %d\n", sum);
	}
}
