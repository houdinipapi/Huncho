#include <stdio.h>

int main(void)
{
	int a = 10, b, c, d;

	b = (a + 1) << 2;
	c = (a + 2) >> 1;
	d = ~(a + 3);

	printf("The value of b is: %d\n", b);
	printf("The value of c is: %d\n", c);
	printf("The value of d is: %d\n", d);

	return (0);
}
