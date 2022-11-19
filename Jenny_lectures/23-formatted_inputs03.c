#include <stdio.h>

/**
  * main - Calculates the mean score
  * Return: Success
  */

int main(void)
{
	float a, b, c, d;

	printf("First student's score: \n");
	scanf("%f", &a);
	printf("Second student's score: \n");
	scanf("%f", &b);
	printf("Third student's score: \n");
	scanf("%f", &c);

	/* Calculating the mean score */
	d = (a + b + c) / 3;
	printf("The mean score is %.2f\n", d);

	return (0);
}
