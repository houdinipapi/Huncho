#include <stdio.h>

/**
 * main - subtracting pointers
 */

void main(void)
{
	int arr[] = { 3, 4, 6, -2, -5};
	int *p = arr;
	int *q = &arr[3];

	printf("q - p is %d\n", q - p);
	printf("p - q is %d\n", p - q);

	printf("Value is: %d\n", *q);

	q = q - 2;
	printf("Value is: %d\n", *q);
}
