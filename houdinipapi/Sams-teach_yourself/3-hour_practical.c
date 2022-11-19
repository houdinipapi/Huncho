#include <stdio.h>

/**
  *integer_subtract - function that performs subtraction
  *main - main function
  *@x: first integer
  *@y: second integer
  *Return: success
  */

int integer_subtract(int x, int y)
{
	int result;

	result = x - y;
	return (result);
}

int main(void)
{
	int value;

	value = integer_subtract(6, 13);
	printf("The subtraction of 6 and 13 is %d.\n", value);
	return (0);
}
