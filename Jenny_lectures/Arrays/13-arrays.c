#include <stdio.h>

/**
  * main - prints array address
  */

void main(void)
{
	int arr[4];
	int i;

	printf("Inserting data elements.\n");

	for (i = 0; i < 4; i++)
	{
		printf("arr[%d]: \n", i);
		scanf("%d", &arr[i]);
	}

	putchar('\n');
	for (i = 0; i < 4; i++)
	{
		printf("%p\n", arr[i]);
	}
}
