#include <stdio.h>

/*
 * main - void pointer
 */

void main(void)
{
	char ch = 'a';
	void *ptr = &ch;

	printf("%c\n", *(char *) ptr);
}
