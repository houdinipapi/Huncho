#include <stdio.h>

/**
  * main - calculates the product of indices in two arrays
  * stores the product in the third array.
  * Return: 0
  */

int main(void)
{
	int a[5], b[5], c[5];
	int i;

	printf("Enter the elements for first array:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);
	}
	printf("Enter the elements for the second array:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &b[i]);
	}

	for (i = 0; i < 5; i++)
	{
		c[i] = a[i] * b[i];

		printf("The product of index %d in both arrays is %d\n", i, c[i]);
	}
	return (0);
}
