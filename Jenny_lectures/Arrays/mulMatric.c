#include <stdio.h>

/**
  * main - matrix multiplication
  * Return: success
  */

int main(void)
{
	int a[3][3], b[3][2], c[3][2];
	int i, j, k, sum;

	printf("Enter elements for the first matrix:\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &a[i][j]);
		}
	}
	printf("Printing the first matrix:\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", a[i][j]);
		}
		putchar('\n');
	}

	printf("Enter the elements of the second matrix:\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 2; j++)
		{
			scanf("%d", &b[i][j]);
		}
	}
	printf("Printing the second matrix:\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d\t", b[i][j]);
		}
		putchar('\n');
	}

	return (0);
}
