/* A program that grades your marks */

#include <stdio.h>

void main(void)
{
	int i;

	printf("Enter your marks: \n");
	scanf("%d", &i);

	if (i > 80)
		printf("Grade A\n");
	else if (i > 70)
		printf("Grade B\n");
	else if (i > 60)
		printf("Grade C\n");

	else
		printf("Your performance is below average!!\n");

	printf("Thank you!\n");
}
