#include <stdio.h>

void sum(int *a, int *b)
{
	int result;
	result = a + b;
	int *ptr1 = &a;
	int *ptr2 = &b;
	a = 5;
	b = 10;

	printf("(Call Function)\na = %d\nb = %d\n", *a, *b);
}

void main(void)
{
	int a = 10, b = 5;
	sum(a, b);
	printf("(Main Function)\na = %d\nb = %d\n", a, b);
}
