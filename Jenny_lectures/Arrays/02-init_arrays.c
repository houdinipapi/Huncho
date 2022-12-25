#include <stdio.h>

/**
  * main -initializing and printing arrays
  */

void main(void)
{
	int a[5], i;

	printf("Enter an integer:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);
	}

	printf("The array items are:\n");
	for (i = 0; i < 5; i++)
	{
		printf("%d\n", a[i]);
	}
}
