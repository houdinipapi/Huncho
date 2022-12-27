#include <stdio.h>

/**
  * main - prints matrices
  */

void main(void)
{
	int arr[3][3];
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("Enter arr[%d][%d]:", i, j);
			scanf("%d", &arr[i][j]);
		}
	}
	printf("\nPrinting the elements in a matrix...\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", arr[i][j]);
			if (j == 2)
			{
				printf("\n");
			}
		}
	}
}
