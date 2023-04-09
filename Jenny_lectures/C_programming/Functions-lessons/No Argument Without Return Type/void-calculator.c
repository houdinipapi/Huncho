#include <stdio.h>

/**
 * calculator() - functionality of a simple calculator
 * main - function that calls the calculator
 * Return: void
 */

void calculator(void);

void main(void)
{
	calculator();
}

void calculator(void)
{
	int a, b;
	int sum, diff, prod, div;

	printf("Enter two numbers:\n");
	scanf("%d%d", &a, &b);

	sum = a + b;
	diff = a - b;
	prod = a * b;
	div = a / b;

	printf("Sum = %d\nDifference = %d\nProduct = %d\nDivision = %d\n", sum, diff, prod, div);
}
