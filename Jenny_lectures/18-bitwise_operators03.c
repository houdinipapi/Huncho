#include <stdio.h>

/**
  * main - bitwise operation
  * Return: success
  */

int main(void)
{
	int a = 9, b = 4;

	printf("%d\n", a & b);
	printf("%d\n", a | b);
	printf("%d\n", a ^ b);
	printf("%d\n", a & b && b + 1 || 0 || b++);
	printf("%d\n", b);

	return (0);
}
