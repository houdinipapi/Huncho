#include <stdio.h>
#include <stdlib.h>

/**
 * main - simple calculations
 * Return: Always 0
 */

int main(void)
{
	int num1, num2;
	int operator;
	int sum, sub, prod, div;

	printf("Enter two numbers: ");
	scanf("%d %d", &num1, &num2);

	printf("Enter an operator: ");
	scanf("%d", &operator);

	if (operator == '+')
	{
		sum = num1 + num2;
		printf("Sum = %d\n", sum);
	}
	if (operator == '-')
	{
		sub = num1 - num2;
		printf("Difference = %d\n", sub);
	}
	if (operator == '*')
	{
		prod = num1 * num2;
		printf("Product = %d\n", prod);
	}
	if (operator == '/')
	{
		div = num1 / num2;
		printf("Division = %d\n", div);
	}
	else
	{
		printf("This calculator only uses +, -, *, and / operators.\nPlease enter a valid one!!\n");
	}

	return (0);
}
