#include <stdio.h>

/**
 * main - functioning of switch statements
 * Return: 0
 */

int main(void)
{
	char grade;

	printf("Enter your grade: ");
	scanf(" %c", &grade);

	switch (grade)
	{
		case 'A':
			{
				printf("Excellent\n");
			}
			break;
		case 'B':
			{
				printf("Good\n");
			}
			break;
		case 'C':
			{
				printf("Average\n");
			}
			break;
		case 'D':
			{
				printf("Poor\n");
			}
			break;
		case 'E':
			{
				printf("Fail\n");
			}
			break;

		default:
			printf("Invalid Grade\n");
	}

	return (0);
}
