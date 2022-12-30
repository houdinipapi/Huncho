#include <stdio.h>

/**
  * main - prints a transpose of a matrix
  */

void main(void)
{
	int arr[2][3];
	int i, j;

	printf("Printing a matrix\n");

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
		}
		putchar('\n');
	}

	printf("TRANSPOSE OF THE MATRIX\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d\t", arr[j][i]);
		}
		printf("\n");
	}
}
