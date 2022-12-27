#include <stdio.h>

/**
  * main - storing elements in a matrix and printing it
  */

void main(void)
{
	/* 2D array declaration */
	int disp[2][3];

	/* Counter variables for the loop */
	int i, j;

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("Enter value for disp[%d][%d]:", i, j);
			scanf("%d", &disp[i][j]);
		}
	}

	/* Displaying array elements */
	printf("Two Dimensional array elements:\n");

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", disp[i][j]);
			if (j == 2)
			{
				printf("\n");
			}
		}
	}
}
