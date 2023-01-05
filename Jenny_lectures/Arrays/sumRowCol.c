#include <stdio.h>

/**
  * main - calculates sum for each row and column in a matrix
  * Return: success
  */

int main(void)
{
	int arr[4][2];
	int i, j, sumRow, sumCol;

	printf("Enter elements for the matrix:\n");
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d\t", arr[i][j]);
		}
		putchar('\n');
	}

	for (i = 0; i < 4; i++)
	{
		sumRow = sumCol = 0;
		for (j = 0; j < 2; j++)
		{
			sumRow = sumRow + arr[i][j];
			sumCol = sumCol + arr[j][i];
		}
		printf("Sum of Rows = %d\nSum of Columns = %d\n", sumRow, sumCol);
	}

	return (0);
}
