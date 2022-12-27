#include <stdio.h>

/**
  * main - printds 2-D arrays
  */

void main(void)
{
	int arr[2][4] = {{23, 32, 64, 46}, {32, 23, 46, 64}};
	int i, j;

	printf("Printing martices...\n");

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 4; j++)
		{
			printf("%d\t", arr[i][j]);
			if (j == 4)
			{
				printf("\n");
			}
		}
	}
}
