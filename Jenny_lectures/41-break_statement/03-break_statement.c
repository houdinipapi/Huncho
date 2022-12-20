#include <stdio.h>

int main(void)
{
	char c;

	for (;;)
	{
		printf("\nPress any key, Q to quit: ");

		// Convert to character value
		scanf("%c", &c);

		if (c == 'Q')
			break;
	}
} // Loop exits only when Q is pressed
