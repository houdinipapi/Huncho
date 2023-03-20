#include <stdio.h>

/**
 * main - subtracting pointers
 */

void main(void)
{
	int arr[] = { 3, 4, 6, -2, -5};
	int *p = a;
	int *q = &a[3];

	printf("q - p is %d\n", q - p);
	printf("p - q is %d\n", p - q);
}
