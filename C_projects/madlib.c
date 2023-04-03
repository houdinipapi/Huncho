#include <stdio.h>
#include <stdlib.h>

/**
 * main - madlib poem
 */

void main(void)
{
	char color[20], noun[10], verb[10];

	printf("Enter a color: ");
	scanf("%s", color);
	printf("Enter a noun: ");
	scanf("%s", noun);
	printf("Enter a verb: ");
	scanf("%s", verb);

	printf("Roses are %s,\n", color);
	printf("%s are blue,\n", noun);
	printf("and I will always %s you.\n", verb);
}
