#include <stdio.h>

/**
  * main - print a transpose
  */

void main(void)
{
	int i, j;
	int arr[2][6] = {{2, 3, 4, 5, 6, 7}, {7, 6, 5, 4, 3, 2}};

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 6; j++)
		{
			printf("%d\t", arr[i][j]);
		}
		putchar('\n');
	}

	for (i = 0; i < 6; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d\t", arr[j][i]);
		}
		putchar('\n');
	}
}
