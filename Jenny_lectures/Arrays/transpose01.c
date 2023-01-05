#include <stdio.h>

/**
  * main - prints a transpose of the matrix
  * Return: success
  */

int main(void)
{
	int arr[4][2];
	int i, j;

	printf("Enter the elements of the matrix:\n");
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	/* Printing the elements of the array */
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d\t", arr[i][j]);
		}
		putchar('\n');
	}

	printf("TRANSPOSE OF THE ABOVE MATRIX IS:\n");
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 4; j++)
		{
			printf("%d\t", arr[j][i]);
		}
		putchar('\n');
	}

	return (0);
}
