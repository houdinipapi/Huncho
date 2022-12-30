#include <stdio.h>

/**
  * main - prints elements of 2D arrays
  * and the sum
  */

void main(void)
{
	int arr[2][3];
	int i, j;
	int sum = 0;

	printf("Enter the elements of 2D arrays:\n");
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("arr[%d][%d]:\n", i, j);
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
		printf("\n");
		printf("%p\n", arr[i]);
		printf("%p\n", arr[j]);
	}
	printf("%d\n", sum);
	printf("%p\n", sum);
}
