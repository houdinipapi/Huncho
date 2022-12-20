#include <stdio.h>

void main(void)
{
	int i = 0;

	do {
		if (i == 7)
		{
			i++;
			continue;
		}
		printf("%d ", i);
		i++;
	} while (i <= 10);
	putchar('\n');
}
