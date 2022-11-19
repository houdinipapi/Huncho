#include <stdio.h>

int main(void)
{
	int a = 1, b = 6, result;

	result = a-- && ++b;
	printf("%d\n", result);
}
