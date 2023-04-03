#include <stdio.h>

/**
 * main - calculates sum of elements
 * Return: success
 */

int main(void)
{
	int matrix[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
	int i, j, sum = 0;

	/* Print the matrix */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 4; j++)
		{
			printf("%d\t", matrix[i][j]);
		}
		printf("\n");
	}

	/* Calculate the sum of all elements */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 4; j++)
		{
			sum += matrix[i][j];
		}
	}

	printf("Sum of all elements: %d\n", sum);
	return (0);
}
