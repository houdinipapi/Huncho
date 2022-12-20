#include <stdio.h>

void main(void)
{
	/* local variable definition */
	int a = 10;

	/* do loop execution */
	do {
		if (a == 15)
		{
			/* skip the iteration */
			++a;
			continue;
		}

		printf("Value of a: %d\n", a);
		++a;
	} while (a < 20);
}
