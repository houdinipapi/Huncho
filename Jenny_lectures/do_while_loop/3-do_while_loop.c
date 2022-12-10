#include <stdio.h>

/**
  * main - print table of numbers
  */

void main(void)
{
	int i = 1, num = 0;

	printf("Enter a number: \n");
	scanf("%d", &num);

	do
	{
		printf("%d\n", (num * i));
		i++;
	}
	while (i < 10);
}
