#include <stdio.h>
/* function that finds the average of numbers  using arrays */

int main(void)
{
	int marks[20], i, n, sum = 0, avg;

	printf("Enter the number of elements: ");
	scanf("%d", &n);

	for (i = 0; i < n; ++i)
	{
		printf("Enter number %d: ", i + 1);
		scanf("%d", &marks[i]);
		sum += marks[i];
	}

	avg = sum / n;
	printf("Avg = %d\n", avg);

	return (0);
}
