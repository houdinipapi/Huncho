#include <stdio.h>

/**
  *main - main function
  *Return: success
  */

int main(void)
{
	int x = 78;
	int y = 34;
	int a;

	a = (y > x) ? x : y;
	printf("%d\n", a);
}
