#include <stdio.h>

/**
  * main - average marks of 5 students
  * Return: 0
  */

int main(void)
{
	int a[5], i;
	float sum = 0, avg;

	printf("Enter your marks:\n");

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &a[i]);
	}
	for (i = 0; i < 5; i++)
	{
		sum = sum + a[i];
	}
	avg = sum / 5;

	printf("Total marks are %.2f and the average is %.2f\n", sum, avg);

	return (0);
}
