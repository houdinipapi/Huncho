#include <stdio.h>

/**
  *product_int - multiplies integers
  *@x: first integer
  *@y: second integer
  *Return: product
  */

int product_int(int x, int y)
{
	int product;

	product = x * y;
	return (product);
}

/**
  *main - main function
  *Return: success
  */

int main(void)
{
	int product;

	product = product_int(3,5);
	printf("The product of 3 multiplied by 5 is %d.\n", product);
	return (0);
}
