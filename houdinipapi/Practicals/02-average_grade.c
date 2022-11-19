#include <stdio.h>

/**
  * main - finds average and grades
  * Return: success
  */

int main(void)
{
	float m1, m2, m3, average;

	printf("Enter marks obtained in Biology: \n");
	scanf("%f", &m1);

	printf("Enter marks obtained in Chemistry: \n");
	scanf("%f", &m2);

	printf("Enter marks obtained in Physics: \n");
	scanf("%f", &m3);

	average = (m1 + m2 + m3) / 3;
	printf("Average: %0.2f\n", average);

	if (average >= 90)
	{
		printf("Grade A\n");
	}

	else if (average >= 80)
	{
		printf("Grade B\n");
	}

	else if (average >= 70)
	{
		printf("Grade C\n");
	}

	else if (average >= 60)
	{
		printf("Grade D\n");
	}

	else
	{
		printf("Grade F\n");
	}

	return (0);
}
