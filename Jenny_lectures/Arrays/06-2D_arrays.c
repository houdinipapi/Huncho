#include <stdio.h>

/**
  * main - prints the subscript of arrays
  */

void main(void)
{
	int arr[3][3] = {{4, 5, 6}, {4, 5, 6}, {4, 5, 6}};
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("arr[%d][%d]\n", i, j);
		}
	}
}
