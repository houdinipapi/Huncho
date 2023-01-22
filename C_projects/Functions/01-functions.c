#include <stdio.h>

/**
 * main - main function
 */

double square(double num)
{
	double result;

	result = num * num;
	return (result);
}

int main(void)
{
	double num;

	printf("Enter a number: ");
	scanf("%lf", &num);

	printf("Answer: %f\n", square(num));

	return (0);
}
