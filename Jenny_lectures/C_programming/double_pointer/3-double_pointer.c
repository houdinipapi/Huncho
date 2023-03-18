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
}
