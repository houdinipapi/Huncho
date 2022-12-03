#include <stdio.h>

/**
  * main - displays output immediately
  * after 10 inputs
  */

int main(void)
{
	// Array declaration
	int rollNo[10];

	// taking input
	for (int i = 0; i < 10; i++)
		scanf("%d", &rollNo[i]);

	// printing output
	for(int i = 0; i < 10; i++)
		printf("%d ", rollNo[i]);

	printf("\n");

	return (0);
}
