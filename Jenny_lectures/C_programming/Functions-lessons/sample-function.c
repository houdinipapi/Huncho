#include <stdio.h>

/**
 * main - function that calls sum
 * sum() - functio that adds two integers
 */

int sum(int x, int y);

void main(void)
{
	int total;
	int x = 15;
	int y = 20;

	total = sum(x, y);

	printf("(Main Function) Sum is %d\n", total);
}

int sum(int x, int y)
{
	return x + y;

	printf("(Called Function) x = %d\ny = %d\n", x, y);
}
