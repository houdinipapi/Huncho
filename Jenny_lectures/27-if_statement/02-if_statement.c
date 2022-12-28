#include <stdio.h>

/**
  * main - prints input in reverse
  */

void main(void)
{
    char i, n;

    printf("Enter an input:\n");
    scanf("%d", &n);
    for (i = (n - 1); i >= 'a'; i--)
    {
        printf("%c ", i);
     }
}
