#include <stdio.h>

/**
 * main - guessing game
 * Return: 0
 */

int main(void)
{
	int luckyNumber;

	do {
		printf("Guess a lucky number: ");
		scanf("%d", &luckyNumber);
	} while (luckyNumber != 7);

	return (0);
}
