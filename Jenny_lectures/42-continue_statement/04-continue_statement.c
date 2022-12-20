#include <stdio.h>

void main(void)
{
	int i = 0;

	while (i <= 10)
	{
		if (i == 6)
		{
			i++;
			continue;
		}
		printf("%d ", i);
		i++;
	}
	putchar('\n');
}
