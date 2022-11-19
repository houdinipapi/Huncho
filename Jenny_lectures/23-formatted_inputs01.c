#include <stdio.h>

int main(void)
{
	int a, b, sum;

	printf("Type two digits: \n");
	scanf("%d %d", &a, &b);

	sum = a + b;
	printf("The sum of your two digits is: %d\n", sum);
	return (0);
}
