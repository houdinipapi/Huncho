/* program that checkes whether a number is odd or even */
#include <stdio.h>

/**
  * main - function that checks odd and even numbers
  * n - integer
  * Return: success
  */

int main(void)
{
	int i;

	printf("Enter a number:\n");
	scanf("%d", &i);

	switch (i % 2)
	{
		case 0:
			printf("EVEN NUMBER\n");
			break;
		default:
			printf("ODD NUMBER\n");
	}
	return (0);
}
