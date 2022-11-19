#include <stdio.h>

/**
  *main - main function
  *Return: success
  */

int main(void)
{
	int a = 50;
	int b = 75;
	int n;

	n = (b < a) ? a : b;
	printf("%d\n", n);
}
