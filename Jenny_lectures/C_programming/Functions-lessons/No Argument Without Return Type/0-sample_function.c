#include <stdio.h>

/**
 * main - main function
 * sum(void) - function with no argument and no return type && adds two numbers.
 */

void sum(void);

void main(void)
{
	sum();
}

void sum(void)
{
	int a, b, sum = 0;

	printf("Enter two numbers:\n");
	scanf("%d%d", &a, &b);

	sum = a + b;

	printf("sum = %d\n", sum);
}
