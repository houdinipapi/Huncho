#include <stdio.h>
#include <stdlib.h>

/**
 * main - checking dangling pointers
*/

void main(void)
{
    int *ptr = NULL;
    int a = 5;
    ptr = &a;

    printf("a = %d\n", *ptr);
}