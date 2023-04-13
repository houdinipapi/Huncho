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
	int sum, prod, diff, division;

	printf("Enter two numbers:\n");
	scanf("%d%d", &a, &b);
