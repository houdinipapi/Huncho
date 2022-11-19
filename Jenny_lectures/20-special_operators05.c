#include <stdio.h>

int main(void)
{
	int a = 8, b;

	b = (a++, ++a, a >> 2);
	printf("The value of a is: %d\n", a);
	printf("The value of b is: %d\n", b);

	return (0);
}
