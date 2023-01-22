#include <stdio.h>

/**
 * greaterNum - function that finds the greatest number
 * main - main function
 * @num1: first input
 * @num2: second input
 * @num3: third input
 * Return: success
 */


int greaterNum(int num1, int num2, int num3)
{
	int max;

	if (num1 > num2 && num1 > num3)
	{
		max = num1;
	}
	else if (num2 > num1 && num2 > num3)
	{
		max = num2;
	}
	else
		max = num3;

	return (max);
}

int main(void)
{
	int num1, num2, num3;

	printf("Enter three numbers: ");
	scanf("%d %d %d", &num1, &num2, &num3);

	printf("Greatest number = %d\n", greaterNum(num1, num2, num3));

	return (0);
}
