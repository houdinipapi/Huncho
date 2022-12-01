#include <stdio.h>
#include "conio.h"

void main(void)
{
	int a;

	printf("Enter a:\n");
	scanf("%d", &a);

	if (a)
		printf("Inside if block\n");

	printf("Outside if block\n");
	getch();
}
