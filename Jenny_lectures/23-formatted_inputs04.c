#include <stdio.h>

int main(void)
{
	int a, b, c, sum, x;

	printf("Key in three different values: \n");

	x = scanf("%d %d %d", &a, &b, &c);
	sum = a + b + c;

	printf("The values you entered are: %d\n", x);
	printf("The sum of your values is: %d\n", sum);

	return (0);
}
