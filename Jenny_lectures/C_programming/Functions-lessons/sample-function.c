#include <stdio.h>

/**
 * main - function that calls sum
 * sum() - functio that adds two integers
 */

void sum(int x, int y);

void main(void)
{
	int total;
	int x = 15;
	int y = 20;

	sum(x, y);

	printf("Sum is %d\n", total);
}

void sum(int x, int y)
{
	int total;
	total = x + y;

	printf("x = %d\ny = %d\n", x, y);
}
