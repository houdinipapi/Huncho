#include <stdio.h>

/**
  * main - print a matrix
  */

void main(void)
{
	int arr[2][3] = {{45, 32, 78}, {54, 23, 87}};
	int i, j;

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", arr[i][j]);
			if (j == 2)
				printf("\n");
		}
	}
}
