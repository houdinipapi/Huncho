#include <stdio.h>

/**
  * main - print array elements
  */

void main(void)
{
	int a[7], i;

	printf("Enter the array elements:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);
	}

	for (i = 0; i < 5; i++)
	{
		printf("Index %d = %d\n", i, a[i]);
	}

	for (i = 4; i >= 0; i--)
	{
		printf("Index %d = %d\n", i, a[i]);
	}
}
