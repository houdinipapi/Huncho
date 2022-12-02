#include <stdio.h>

void main(void)
{
	int age;

	printf("Enter your age:\n");
	scanf("%d",&age);

	if (age > 20 && age < 30)
	{
		printf("Your age is %d and you are eligible.\n", age);
	}
	printf("Your age is %d and you are not eligible.\n", age);
}
