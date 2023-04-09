#include <stdio.h>

/**
 * sum() - addition
 * difference() - subtraction
 * product() - multiplication
 * division() - division
 * main - main function
 * Return: void
 */

void sum(void);
void difference(void);
void product(void);
void division(void);

void main(void)
{
	sum();
	difference();
	product();
	division();
}

void sum(void)
{
	int a, b, sum;

	printf("Enter two numbers:\n");
	scanf("%d%d", &a, &b);

	sum = a + b;
	printf("Sum = %d\n", sum);
}
