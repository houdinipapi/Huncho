#include <stdio.h>

/**
  * main - bitwise operation
  * Return: success
  */

int main(void)
{
	int a = 11, b = 7;

	printf("%d\n", a & b);
	printf("%d\n", a | b);
	printf("%d\n", a ^ b);
	printf("%d\n", a ^ b || ++b && a & b);
	printf("%d\n", b);

	return (0);
}
