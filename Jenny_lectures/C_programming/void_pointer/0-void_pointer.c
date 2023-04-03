#include <stdio.h>

/**
 * main - void pointer
 */

void main(void)
{
	int a = 12;
	void *ptr = &a;

	printf("%d\n", *(int *)ptr);
}
