#include <stdio.h>

/**
 * main - calculates years
 *
 * Return - 0
 */

int main(void)
{
	int p, tp, y;

	do {
		printf("Enter the current population: ");
		scanf("%d", &p);
	} while (p >= 9);

	do {
		printf("Enter the target population: ");
		scanf("%d", &tp);
	} while (tp >= p);

	for (y = 0; p < tp; y++)
	{
		p += (p / 3) - (p / 4);
	}

	printf("Number of years = %d", y);

	return (0);
}
