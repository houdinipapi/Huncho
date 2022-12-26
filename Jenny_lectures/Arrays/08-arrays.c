#include <stdio.h>

/**
  * main - adds odd numbers and even numbers separately
  * Return: 0;
  */

int main(void)
{
	int a[5], i;
	int even = 0, odd = 0;
	int sumEven = 0, sumOdd = 0;

	printf("Enter numbers:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);

		if (a[i] % 2 == 0)
		{
			even++;
			sumEven = sumEven + a[i];
		}
		else
		{
			odd++;
			sumOdd = sumOdd + a[i];
		}
	}
	printf("Even numbers are %d and their total sum is %d\n", even, sumEven);
	printf("Odd numbers are %d and their total sum is %d\n", odd, sumOdd);

	return (0);
}
