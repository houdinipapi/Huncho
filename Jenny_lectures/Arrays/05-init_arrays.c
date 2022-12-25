#include <stdio.h>

/**
  * main - calculates sum and average of array elements
  */

void main(void)
{
	int marks[7], i;
	float avg, sum = 0;

	printf("Enter the students' marks:\n");
	for (i = 0; i < 7; i++)
	{
		scanf("%d", &marks[i]);
	}

	/* Calculating the sum */

	for (i = 0; i < 7; i++)
	{
		sum = sum + marks[i];
	}
	avg = sum / 7;
	printf("Total Sum is %f and the average is %f\n", sum, avg);
}
