#include <stdio.h>

void main(void)
{
	int age;

	printf("Enter your age:\n");
	scanf("%d",&age);

	if (age > 15)
	{
		printf("You are eligible.\n");
	}
	printf("Your age is %d\n", age);
}
