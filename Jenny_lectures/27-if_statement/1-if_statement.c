#include <stdio.h>

int main(void)
{
	int a, b, c;

	printf("Enter three numbers\na: ");
	scanf("%d", &a);
	printf("\nb: ");
	scanf("%d", &b);
	printf("\nc: ");
	scanf("%d", &c);

	if (a > b && a > c)
	{
		printf("%d is the greatest\n", a);
	}
	if (b > a && b > c)
	{
		printf("%d is the greatest\n", b);
	}
	if (c > a && c > b)
	{
		printf("%d is the greatest\n", c);
	}

	return (0);
}
