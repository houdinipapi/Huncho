#include <stdio.h>

void main(void)
{
	int a = 5, b, c, d;

	b = ++a;
	c = a++;
	d = ++a;
	printf("The value of a is %d.\n", a);
	printf("The value of b is %d.\n", b);
	printf("The value of c is %d.\n", c);
	printf("The value of d is %d.\n", d);
}
