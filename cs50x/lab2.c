#include <stdio.h>

/**
 * main - calculates years
 * Return: success
 */

int main(void)
{
	int population, target_population, years;

	/* Getting starting population from the user */
	printf("Enter the starting population: ");
	scanf("%d", &population);

	/* target population */
	printf("Enter the target population: ");
	scanf("%d", &target_population);

	for (years = 0; population < target_population; years++)
	{
		population = population + (population / 3) - (population / 4);
	}

	printf("It will take %d years to reach the target population.\n", years);

	return (0);
}
