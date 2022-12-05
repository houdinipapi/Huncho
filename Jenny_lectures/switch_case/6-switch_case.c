#include <stdio.h>

/**
  * main - a claculator program
  * @a: first input
  * @b: second input
  * @sum: addition
  * @diff: subtraction
  * @prod: multiplication
  * @div: division
  * @operator: character representing an operator
  */

void main(void)
{
	int a, b, sum, diff, prod;
	int div;
	char operator;

	printf("Enter an operator:\n");
	scanf("%c", &operator);

	printf("Enter two operands:\n");
	scanf("%d %d", &a, &b);

	switch (operator)
	{
		case '+':
			{
				sum = a + b;
				printf("Sum is %d\n", sum);
			}
			break;
		case '-':
			{
				diff = a - b;
				printf("Difference is %d\n", diff);
			}
			break;
		case '*':
			{
				prod = a * b;
				printf("Product is %d\n", prod);
			}
			break;
		case '/':
			{
				div = a / b;
				printf("Value is %d\n", div);
			}
			break;
		default:
			printf("Enter a valid operator!!\n");
	}
}
