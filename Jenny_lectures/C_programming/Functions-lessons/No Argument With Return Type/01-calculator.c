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
	int a, b, c;
	//int sum, prod, diff, division;

	printf("Enter two numbers and a calculation index(1.sum, 2.prod, 3.diff, 4.division):\n");
	scanf("%d%d%d", &a, &b, &c);

	if (c == 1)
	{
		return (a + b);
	}
	else if (c == 3)
	{
		return (a - b);
	}
	else if (c == 2)
	{
		return (a * b);
	}
	else if (c == 4)
	{
		return (a / b);
	}
	else
		printf("Enter Valid Operator Index\n");
}
