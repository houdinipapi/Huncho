#include <stdio.h>

/**
 * main - incrementing and decrementing pointers;
 */

void main(void)
{
	int arr[] = {10, 11, -1, 56, 67, 5, 4};
	int *p, *q;

	p = arr;

	printf("%d\n", *p);

	printf("%d %d %d\n", (*p)++, *p++, *++p);

	q = p + 3;

	printf("%d\n", *q - 3);
	printf("%d\n", *--p + 5);
	printf("%d\n", *p + *q);
}
