#include <stdio.h>

/**
  * main - prints the number pattern
  */

void main(void)
{
	int i = 0, j;

	while (i <= 10)
	{
		j = 0;
		while (j <= i)
		{
			printf("%d ", j);
			j++;
		}
		printf("\n");
		i++;
	}
}
