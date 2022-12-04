/* A program that prints weekdays */

#include <stdio.h>
/**
  * main - function that prints days of a week
  * num - input
  * Return: 0
  */

int main(void)
{
	int num;

	printf("Enter a number:\n");
	scanf("%d", &num);

	switch (num)
	{
		case 1:
			printf("Sunday\n");
			break;
		case 2:
			printf("Monday\n");
			break;
		case 3:
			printf("Tuesday\n");
			break;
		case 4:
			printf("Wednesday\n");
			break;
		case 5:
			printf("Thursday\n");
			break;
		case 6:
			printf("Friday\n");
			break;
		case 7:
			printf("Saturday\n");
			break;
		default:
			printf("The number does not match any week day!!\n");
	}
	return (0);
}
