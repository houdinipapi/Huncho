#include <stdio.h>

/**
  * main - reverse numbers using while function
  */

void main(void)
{
	int i;

	printf("Enter a number:\n");
	scanf("%d", &i);

	while (i >= 0)
	{
		printf("%d, ", i);
		i = i - 1;
	}

	putchar('\n');
}
