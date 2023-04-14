#include <stdio.h>

int calculator(void);

/**
 * main - calls the calculator function
 */

void main(void)
{
	calculator();
}

/**
 * calculator - simple calculations
 * Return: Success
 */

int calculator(void)
{
	int a, b;
	char c;
	int sum, prod, diff, division;

	printf("Enter two numbers and a calculation sign(sum, prod, diff, division):\n");
	scanf("%d%d%s", &a, &b, c);

	if (c == 'sum')
	{
		return (a + b);
	}
	else if (c == 'diff')
	{
		return (a - b);
	}
	else if (c == 'prod')
	{
		return (a * b);
	}
	else if (c == 'division')
	{
		return (a / b);
	}
	else
		printf("Enter Valid Operator\n");
}
