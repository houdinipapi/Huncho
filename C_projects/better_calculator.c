#include <stdio.h>

/**
 * main - a better calculator
 * Return: 0
 */

int main(void)
{
	int num1, num2;
	char operator;

	printf("Enter two numbers:\n");
	scanf("%d %d", &num1, &num2);

	printf("Enter an operator: ");
	scanf(" %c", &operator);

	if (operator == '+')
	{
		printf("Sum = %d\n", num1 + num2);
	}
	else if (operator == '-')
	{
		printf("Difference = %d\n", num1 - num2);
	}
	else if (operator == '/')
	{
		printf("Division = %d\n", num1 / num2);
	}
	else if (operator == '*')
	{
		printf("Product = %d\n", num1 * num2);
	}

	else
		printf("Invalid Operator!!\n");


	return (0);
}
