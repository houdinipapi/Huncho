#include <stdio.h>

void main(void)
{
	int age, salary;

	printf("Enter your age and salary:\n");
	scanf("%d %d", &age, &salary);

	if (age > 50)
	{
		if (salary < 60000)
		{
			salary = salary + 10000;
		}
		else
		{
			salary = salary + 5000;
		}
	}
	else
	{
		salary = salary + 3000;
	}

	printf("Your new salary is %d\n", salary);
}
