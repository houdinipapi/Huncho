#include <stdio.h>

void main(void)
{
	/* local variable definition */
	int a = 10;

	/* while loop execution */
	while (a < 20)
	{
		printf("Value of a: %d\n", a);
		a++;

		if (a > 15)
		{
			/* terminate the loop using break statement */
			break;
		}
	}
}
