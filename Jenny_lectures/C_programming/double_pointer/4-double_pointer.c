#include <stdio.h>

/**
 * main - pointers
 */

void main(void)
{
	int a = 25;
	int *p = &a;
	int **q = &p;
	int ***r = &q;

	printf("a = %d\n", a);
	printf("a = %d\n", *p);
	printf("a = %d\n", **q);
	printf("a = %d\n", ***r);

	printf("Address of a = %x\t%x\n", &a, p);
	printf("Address of p = %x\t%x\n", &p, q);
	printf("Address of q = %x\t%x\n", &q, r);
}
