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
		printf("%d is the greatest number\n");
	}
	else if (j > i && j > k)
	{
		printf(
