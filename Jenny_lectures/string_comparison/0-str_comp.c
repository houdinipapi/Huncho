#include <stdio.h>
#include <string.h>

/**
 * main - string comparison
 */

void main(void)
{
	char your_name[30];
	char friend_name[30];
	int value;

	printf("Enter your name and your friend's name:\n");
	scanf("%s %s", your_name, friend_name);

	value = strcmp(your_name, friend_name);

	if (value == 0)
	{
		printf("Same\n");
	}
	else
	{
		printf("Not Same\n");
	}

	printf("%d\n", value);
}
