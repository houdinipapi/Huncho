#include <stdio.h>

void printMatrix(int matrix[3][4])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 4; j++)
		{
			printf("%d\t", matrix[i][j]);
		}
		printf("\n");
	}
}

void transposeMatrix(int matrix[3][4])
{
	int i, j, temp;

	for (i = 0; i < 3; i++)
	{
		for (j = i; j < 4; j++)
		{
			temp = matrix[i][j];
			matrix[i][j] = matrix[j][i];
			matrix[j][i] = temp;
		}
	}
}

int main(void)
{
	int matrix[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

	printf("Original Matrix:\n");
	printMatrix(matrix);

	transposeMatrix(matrix);

	printf("Transposed matrix:\n");
	printMatrix(matrix);

	return (0);
}
