#include <stdio.h>

/**
  * main - prints the address of arrays
  */

void main(void)
{
	int arr[2][3];
	int i, j;

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("Enter the values for arr[%d][%d]", i, j);
			scanf("%d", &arr[i][j]);
		}
	}
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", arr[i][j]);
			if (j == 2)
				putchar('\n');
		}
	}
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("arr[%d][%d]\t %d\t %p", i, j, arr[i][j], arr[i][j]);
			putchar('\n');
		}
	}
}
