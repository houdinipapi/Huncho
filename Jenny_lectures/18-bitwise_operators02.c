#include <stdio.h>

/**
  * main - bitwise operations
  * Return: success
  */

int main(void)
{
	int a = 10, b = 6;

	printf("%d\n", a & b);
	printf("%d\n", a | b);
	printf("%d\n", a ^ b);
	printf("%d\n", a & b && b + 1 || 0 || b++);
	printf("%d\n", b);

	return (0);
}
