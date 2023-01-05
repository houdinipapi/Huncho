#include <stdio.h>

/**
  * main - calculates the total sum of the matrix
  * Return: success
  */

int main(void)
{
	int arr[2][3];
	int i, j, sum = 0;

	printf("Enter elements of the array:\n");
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}
	printf("The matrix of the elements is:\n");
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", arr[i][j]);
			sum = sum + arr[i][j];
		}
		putchar ('\n');
	}
	printf("SUM = %d\n", sum);

	return (0);
}
