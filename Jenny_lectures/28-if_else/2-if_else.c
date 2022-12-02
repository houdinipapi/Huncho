#include <stdio.h>

int main(void)
{
	int age;

	printf("Enter your age:\n");
	scanf("%d", &age);

	if (age >= 25 && age <= 30)
	{
		printf("Your age is %d.\n", age);
		printf("You are eligible\n");
	}
	else
	{
		printf("Your age is %d.\n", age);
		printf("You are not eligible.\n");
	}
	printf("Thank you for your time!\n");
}
