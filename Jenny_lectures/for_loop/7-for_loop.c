#include <stdio.h>

/**
  * main - prints a multiplication table
  */

void main(void)
{
	int i, num;

	printf("Enter a number:\n");
	scanf("%d", &num);

	for (i = 1; i <= 10; i++)
	{
		printf("%d by %d = %d\n", num, i, num * i);
	}
}
