#include <stdio.h>

/**
 * main - guessing game
 * Return: 0
 */

int main(void)
{
	int luckyNumber;
	int guessTimes = 0;

	do {
		printf("Guess a Lucky Number: ");
		scanf("%d", &luckyNumber);
		guessTimes++;
	} while (luckyNumber != 7);

	if (luckyNumber == 7)
	{
		printf("YEES!! That's our LUCKY NUMBER!!\n");
	}
	return (0);
}
