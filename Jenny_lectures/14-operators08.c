#include <stdio.h>

void main(void)
{
	int x = 10, y;

	y = x--;
	printf("The value of x is %d.\n", x);
	printf("The value of y is %d.\n", y);
}
