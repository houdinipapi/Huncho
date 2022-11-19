#include <stdio.h>

int main(void)
{
	int a, b, sum, x;
	char c;

	printf("Key in three different data types: \n");

	x = scanf("%d %d %c", &a, &b, &c);
	sum = a + b;

	printf("The values you entered are: %d\n", x);
	printf("The sum of your values is: %d and the character is: %c\n", sum, c);

	return (0);
}
