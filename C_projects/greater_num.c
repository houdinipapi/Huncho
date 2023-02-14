#include <stdio.h>

/**
 * main - checks for a greater number
 */

void main(void)
{
	int i, j, k;

	printf("Enter three numbers: ");
	scanf("%d %d %d", &i, &j, &k);

	if (i > j && i > k)
	{
		printf("%d is the greatest number\n", i);
	}
	else if (j > i && j > k)
	{
		printf("%d is the greatest number\n", j);
	}
	else if (k > i && k > j)
	{
		printf("%d is the greatest number\n", k);
	}
	else
		printf("All numbers are equal\n");
}
