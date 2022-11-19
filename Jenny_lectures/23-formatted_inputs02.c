#include <stdio.h>

int main(void)
{
	char a[20];
	int b;
	float c, d;

	printf("Name: \n");
	scanf("%s", a);
	printf("Weight: \n");
	scanf("%d", &b);
	printf("Height: \n");
	scanf("%f", &c);

	d = (b + c) / 2;

	printf("Hello %s, your weight is %d, your height is %f and your BMI is %f.", a, b, c, d);

	return (0);
}
