#include <stdio.h>

/**
 * main - post increment of pointers
 */

void main(void)
{
	int arr[] = {3, 5, 6, -7, 4, 9};
	int *p = arr[5];

	p--;
	printf("%d\n", *p);
}
