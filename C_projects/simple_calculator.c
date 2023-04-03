#include <stdio.h>
#include <stdlib.h>

/**
 * main - simple calculations
 * Return: Always 0
 */

int main(void)
{
	int num1, num2;
	char operator;
	int sum, sub, prod, div;

	printf("Enter an operator: ");
	scanf("%c", &operator);

	printf("Enter two numbers: ");
	scanf("%d %d", &num1, &num2);

	switch (operator)
	{
		case '+':
			{
				sum = num1 + num2;
				printf("Sum = %d\n", sum);
			}
			break;
		case '-':
			{
				sub = num1 - num2;
				printf("Difference = %d\n", sub);
			}
		case '*':
			{
				prod = num1 * num2;
				printf("Product = %d\n", prod);
			}
			break;
		case '/':
			{
				div = num1 / num2;
				printf("Division = %d\n", div);
			}
			break;
		default:
				printf("Enter a valid operator\n");
	}
	return (0);
}
