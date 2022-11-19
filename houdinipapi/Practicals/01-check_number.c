#include <stdio.h>
// #include <conio.h>

/**
  * main - accepts and checks whether a number is positive, negative or zero
  * Return: success
  */

void main(void)
{
	int n;

	// clrscr();

	printf("Enter number: \n");
	scanf("%d", &n);

	if (n > 0)
		printf("Number is positive\n");

	else if (n < 0)
		printf("Number is negative\n");

	else
		printf("Number is Zero\n");

	// getc();

	// return (0);
}
