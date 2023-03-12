#include <stdio.h>

/**
 * main - pointers and addresses
 */

void main(void)
{
	unsigned int a = 10;
	unsigned int b = 15;
	int *p = &a;
	int *q = &b;

	printf("Address of a is %u\n", &a);
}
