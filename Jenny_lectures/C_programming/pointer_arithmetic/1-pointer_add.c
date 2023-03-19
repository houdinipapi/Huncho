#include <stdio.h>

/**
 * main - addition of pointers
 */

void main(void)
{
	int a[7] = {1, -5, 6, 4, -3, 2, 9};
	int *p = &a[0];

	printf("Value is: %d\n", *p);
}
