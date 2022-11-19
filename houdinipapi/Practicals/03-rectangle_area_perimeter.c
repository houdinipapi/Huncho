#include <stdio.h>

/**
  * main - finds area and perimeter of rectangle
  * Return: success
  */

int main(void)
{
	float length, breadth, area, perimeter;

	printf("Rectangle length = \n");
	scanf("%f", &length);

	printf("Rectangle breadth = \n");
	scanf("%f", &breadth);

	/* Calculating area and perimeter */
	area = length * breadth;
	perimeter = 2 * (length + breadth);

	/* Displaying the result */
	printf("Area of rectangle = %f\n", area);
	printf("Perimeter of rectangle = %f\n", perimeter);

	return (0);
}
