#include <stdio.h>

/**
  * main - prints a transpose of an array
  */

void main(void)
{
	int arr[4][5];
	int i, j;

	printf("Enter elements:\n");
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 5; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	printf("The elements in a matrix are:\n");
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 5; j++)
		{
			printf("%d\t", arr[i][j]);
			if (j == 4)
			{
				printf("\n");
			}
		}
	}

	printf("The transpose of the matrix is:\n");
	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 4; j++)
		{
			printf("%d\t", arr[j][i]);
		}
		putchar('\n');
	}
}
