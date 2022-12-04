/* a program that grades students */
#include <stdio.h>

int main(void)
{
	int i;

	printf("Enter your marks:\n");
	scanf("%d", &i);

	switch(i / 10)
	{
		case 10 :
		case 9 :
			printf("Your Grade is A\n");
			break;
		case 8 :
		case 7 :
			printf("Your Grade is B\n");
			break;
		case 6 :
		case 5 :
			printf("Your Grade is C\n");
			break;
		case 4 :
			printf("Your Grade is D\n");
			break;
		default :
			printf("You failed!\n");
	}

	return (0);
}
