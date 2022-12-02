#include <stdio.h>

int main(void)
{
	int a;

	printf("Enter a number:\n");
	scanf("%d", &a);
	printf("You entered %d\n", a);

	if (a > 0)
		printf("%d is a positive number\n", a);
	else
		printf("%d is a negative number\n", a);
}
