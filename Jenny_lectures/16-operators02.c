#include <stdio.h>

int main(void)
{
	int a = 7, b = 16, c, d, e = 13;

	c = ++b;
	d = b;
	printf("%d\n", a < b < c > d);
	printf("%d\n", b == e);
	printf("%d\n", c + 1 > e);
	printf("%d\n", a + c == b > e < c + d);
}
