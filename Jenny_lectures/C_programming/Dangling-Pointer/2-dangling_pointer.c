#include <stdio.h>
#include <stdlib.h>

/**
 * main - checking for dangling pointers
*/

int *f()
{
    int a = 9;
    return &a;
}

void main(void)
{
    int *ptr = f();

    printf("%d\n", *ptr);
}