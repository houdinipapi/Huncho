#include <stdio.h>

/**
  *main - main function
  *Return: success
  */

int main(void)
{
	int y = 10;
	int x = 11;

	y = ++x;
	printf("%d\n", y);
	printf("%d\n", x);
}
