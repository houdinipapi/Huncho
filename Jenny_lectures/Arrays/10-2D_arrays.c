#include <stdio.h>

/**
  * main - prints sum of each row and column
  */

void main(void)
{
	int arr[3][3];
	int i, j, sumR, sumC;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	/* Printing the array */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", arr[i][j]);
		}
		putchar('\n');
	}

	/* Printing the sum of each row and column */
	for (i = 0; i < 3; i++)
	{
		sumR = sumC = 0;
		for (j = 0; j < 3; j++)
		{
			sumR = sumR + arr[i][j];
			sumC = sumC + arr[j][i];
		}
		printf("Sum of rows = %d\n Sum of columns = %d\n", sumR, sumC);
	}
}
