#include <stdio.h>

void main(void)
{
	int i, j;

	for (i = 1, j = 0; i < 5, j < 3; i++, j++)
	{
		printf("%d %d\n", j, i);
	}
}
