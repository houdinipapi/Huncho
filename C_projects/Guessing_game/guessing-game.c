#include <stdio.h>

/**
 * main - guessing game
 * Return: 0
 */

int main(void)
{
	int luckyNumber;
	int guessTimes;

	if (guessTimes > 3)
	{
		do {
			printf("Guess a lucky number: ");
			scanf("%d", &luckyNumber);
		} while (luckyNumber != 7);

		if (luckyNumber == 7)
		{
			printf("YEES!! That's our LUCKY NUMBER!!\n");
		}
	}
	else
	{
		printf("You have run out of guesses\n");
	}

	return (0);
}
