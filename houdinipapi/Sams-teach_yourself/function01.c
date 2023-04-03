#include <stdio.h>

/**
 * main - returns a product of two numbers
 */

int myFunction(int x, int y)
{
	int result = x * y;

	return result;
}

int main(void)
{
	int x, y, product;

	printf("Enter two numbers: \n");
	scanf("%d %d", &x, &y);

	product = myFunction(x, y);
	printf("The multiplication of %d and %d is %d\n", x, y, product);

	return (0);
}
