#include <stdio.h>

/**
 * main - void pointer
 */

void main(void)
{
	void *ptr = 12;
	//int a = 12;

	printf("%d\n", *(int *)ptr);
}
