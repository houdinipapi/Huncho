#include <stdio.h>
#include <string.h>

/**
 * main - string comparison without a predefined function
 */

void main(void)
{
	char first_name[30];
	char second_name[15];
	int i, flag = 0;

	printf("Enter two names:\n");
	scanf("%s %s", first_name, second_name);

	for (i = 0; first_name[i] != '\0' && second_name[i] != '\0'; i++)
	{
		if (first_name[i] != second_name[i])
		{
			flag = 1;
			break;
		}
	}
	if (flag == 1)
	{
		printf("Not Same\n");
	}
	else
	{
		printf("Same\n");
	}
}
