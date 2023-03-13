#include <stdio.h>

/**
 * main - pointers and addresses
 */

void main(void)
{
	int a = 10;
	int b = 15;
	int *p, *q;

	p = &a;
	q = &b;

	printf("a is %d\n", *p);
	printf("a is %d\n", a);
}
