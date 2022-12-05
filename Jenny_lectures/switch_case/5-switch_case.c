#include <stdio.h>

/**
  * main - finds the maximum number
  * @a - integer
  * @b - integer
  * Return: Success
  */

int main(void)
{
	int a, b;

	printf("Enter two numbers:\n");
	scanf("%d %d", &a, &b);

	switch (a / b)
	{
		case 0:
			printf("%d is the maximum number.\n", b);
			break;
		default:
			printf("%d is the maximum number.\n", a);
	}
	return (0);
}
