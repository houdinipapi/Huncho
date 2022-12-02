#include <stdio.h>

int main(void)
{
	int a, b, c;

	printf("Enter the value of a, b & c\n");
	scanf("%d %d %d", &a, &b, &c);
	printf("The numbers are %d, %d, and %d\n", a, b, c);

	if (a > b && a > c)
	{
		printf("%d is the greatest\n", a);
	}
	else if(b > c && b > a)
	{
		printf("%d is the greatest\n", b);
	}
	else
		printf("%d is the greatest number\n", c);
}
