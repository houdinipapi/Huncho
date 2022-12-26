#include <stdio.h>

/**
  * main - counts even numbers and odd numbers
  * Return: 0
  */

int main(void)
{
	int a[10], i;
	int even = 0, odd = 0;

	printf("Enter numbers:\n");

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &a[i]);
	}
	for (i = 0; i < 10; i++)
	{
		if (a[i] % 2 == 0)
			even++;
		else
			odd++;
	}
	printf("The even numbers are %d\n", even);
	printf("The odd numbers are %d\n", odd);

	return (0);
}
