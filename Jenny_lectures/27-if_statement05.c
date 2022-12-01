#include <stdio.h>
#include "conio.h"

void main(void)
{
	int age;

	printf("Enter your age:\n");
	scanf("%d", &age);

	if (age > 18)
	{
		printf("You are %d years old.\n", age);
		printf("You are allowed to vote.\n");
	}

	printf("You are a patriot!\n");
	getch();
}
