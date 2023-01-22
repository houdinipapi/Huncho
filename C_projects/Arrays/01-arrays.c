#include <stdio.h>

/**
 * main - arrays
 * Return: Always 0
 */

int main(void)
{
	int age[5];
	int i;

	printf("Enter age of pupils: ");
	for (i = 1; i <= 5; i++)
	{
		scanf("%d", &age[i]);
	}

	return (0);
}
