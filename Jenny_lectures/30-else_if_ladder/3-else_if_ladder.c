/* Program to check a leap year */
#include <stdio.h>

int main(void)
{
	int year;

	printf("Insert a year:\n");
	scanf("%d", &year);

	if (year % 4 == 0)
	{
		if (year % 100 == 0)
		{
			if (year % 400 == 0)
			{
				printf("LEAP year\n");
			}
			else
				printf("NOT a leap year.\n");
		}
		else
			printf("LEAP year.\n");
	}
	else
		printf("NOT a leap year.\n");

	return (0);
}
