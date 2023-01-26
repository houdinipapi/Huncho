#include <stdio.h>

/**
 * main - guessing game
 * Return: 0
 */

int main(void)
{
	int luckyNumber;
	int guessTimes;

	for (guessTimes = 0; guessTimes < 3; guessTimes++)
	{
		printf("Guess a Lucky Number: ");
		scanf("%d", &luckyNumber);

		if (luckyNumber == 7)
		{
			printf("YEESS!! That's our Lucky Number!!\n");
		}
	}
	if (guessTimes >= 3)
	{
		printf("OUT OF GUESSES\n");
	}
	else
	{
		printf("GAME OVER!!!\n");
	}

	return (0);
}
