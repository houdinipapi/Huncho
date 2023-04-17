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

void difference(void)
{
	int x, y, difference;

	printf("Enter two numbers:\n");
	scanf("%d%d", &x, &y);

	difference = x - y;
	printf("Difference = %d\n", difference);
}

void product(void)
{
	int j, k, product;

	printf("Enter two numbers:\n");
	scanf("%d%d", &j, &k);

	product = j * k;
	printf("Product = %d\n", product);
}

void division(void)
{
	float m, n, division;

	printf("Enter two numbers:\n");
	scanf("%f%f", &m, &n);

	division = m / n;
	printf("Division = %f\n", division);
}
