#include <stdio.h>

/**
  * main - prints array items in reverse order
  */

void main(void)
{
	int a[5], i;

	printf("Enter array items:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);
	}

	printf("The items in reverse order are:\n");

	for (i = 4; i >= 0; i--)
	{
		printf("%d\n", a[i]);
	}
}
