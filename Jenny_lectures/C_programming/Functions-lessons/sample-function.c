#include <stdio.h>

/**
 * main - function that calls sum
 * sum() - functio that adds two integers
 */

void sum(int x, int y);

void main(void)
{
	int x = 15;
	int y = 20;

	sum(x, y);

	printf("Sum is %d\n", sum);
}

void sum(int x, int y)
{
	sum = x + y;
	printf("x = %d\ny = %d\n", x, y);
}
