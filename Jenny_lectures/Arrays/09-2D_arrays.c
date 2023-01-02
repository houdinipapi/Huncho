#include <stdio.h>

/**
  * main - prints sum of a matrix
  */

void main(void)
{
	int arr[2][3];
	int i, j, sum = 0;

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", arr[i][j]);
			sum = sum + arr[i][j];
		}
		putchar('\n');
	}
	printf("SUM = %d\n", sum);
}
