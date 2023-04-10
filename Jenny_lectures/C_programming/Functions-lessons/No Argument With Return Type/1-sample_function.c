#include <stdio.h>

// Function Declaration
int sum(void);

/**
 * main - function that calls the user-defined function
 */

void main(void)
{
	int x;

	x = sum();

	printf("Sum = %d\n", x);
}

/**
 * int sum(void) - Function that adds numbers
 * Return: sum
 */

int sum(void)
{
	int a, b, sum;

	printf("Enter two numbers:\n");
	scanf("%d%d", &a, &b);

	sum = a + b;

	return (sum);
}
