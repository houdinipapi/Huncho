#include <stdio.h>

/**
 * main - guessing game
 * Return: 0
 */

int main(void)
{
	int luckyNumber;
	int guessTimes = 1;

	do {
		printf("Guess a Lucky Number: ");
		scanf("%d", &luckyNumber);
		guessTimes++;
	} while (guessTimes > 3);

	if (guessTimes > 3)
	{
		printf("OUT OF GUESSES!!!\n");
	}
	if (luckyNumber == 7)
	{
		printf("YEES!! That's our LUCKY NUMBER!!\n");
	}
	return (0);
}
