#include <stdio.h>

/**
  * main - prints the subscript of arrays
  */

void main(void)
{
	int arr[3][3] = {{4, 5, 6}, {4, 5, 6}, {4, 5, 6}};
	int i, j;

	printf("These are the subscript values of this array:\n");
	putchar('\n');

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("arr[%d][%d]\n", i, j);
		}
	}

	printf("Printing the values of the array\n");
	putchar('\n');

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
