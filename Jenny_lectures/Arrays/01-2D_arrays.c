#include <stdio.h>

/**
  * main - storing elements in a matrix and printing it
  * Return: 0
  */

int main(void)
{
	int arr[2][5];
	int i, j;

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 5; j++)
		{
			printf("Enter a[%d][%d]:\n", i, j);
			scanf("%d", &arr[i][j]);
		}
	}
	printf("printing elements ...\n");

	for (i = 0; i < 2; i++)
	{
		//printf("\n");
		for (i = 0; j < 5; j++)
		{
			printf("%d\t", arr[i][j]);
		}
	}
	return (0);
}
