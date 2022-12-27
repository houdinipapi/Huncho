#include <stdio.h>

/**
  * main - prints a matrix
  */

void main(void)
{
	int arr[3][2];
	int i, j;

	/* Taking Input */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("Enter the value for arr[%d][%d]:", i, j);
			scanf("%d", &arr[i][j]);
		}
	}

	/* Displaying Output */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d\t", arr[i][j]);
			if (j == 1)
			{
				printf("\n");
			}
		}
	}
}
