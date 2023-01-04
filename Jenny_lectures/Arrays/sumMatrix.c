#include <stdio.h>

/**
  * main - sum of two matrices
  * Return: success
  */

int main(void)
{
	int a[2][3], b[2][3], c[2][3];
	int i, j;

	printf("Entering and Printing elements for a[i][j]\n");
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &a[i][j]);
		}
	}

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", a[i][j]);
		}
		putchar('\n');
	}

	printf("Entering and Printing elements for b[i][j]\n");
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			scanf("%d", &b[i][j]);
		}
	}

	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d\t", b[i][j]);
		}
		putchar('\n');
	}

	/* Printing the sum matrix */
	for (i = 0; i < 2; i++)
	{
		for (j = 0; j < 3; j++)
		{
			c[i][j] = a[i][j] + b[i][j];
			printf("%d\t", c[i][j]);
		}
		putchar('\n');
	}
	return (0);
}
