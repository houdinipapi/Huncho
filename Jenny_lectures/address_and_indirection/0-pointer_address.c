#include <stdio.h>

/**
 * main - pointers and addresses
 */

void main(void)
{
	int a = 10;
	int b = 15;
	int *p, int *q;

	p = &a;
	q = &b;

	printf("Address of a is %x\n", &a);
}
