/* A program that identifies the input */

#include <stdio.h>

void main(void)
{
	char a;

	printf("Insert a single element:\n");
	scanf("%c", &a);

	if (a >= 'A' && a <= 'Z')
		printf("Your entered %c and it is an UPPERCASE.\n", a);
	else if (a >= 'a' && a <= 'z')
		printf("You entered %c and it is a lowercase.\n", a);
	else if (a >= '0' && a <= '9')
		printf("You entered %c and it is a digit.\n", a);

	else
		printf("You entered %c and it is a special character.\n", a);
}
