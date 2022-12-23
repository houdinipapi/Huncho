#include <stdio.h>
#include "main.h"

/**
  * _isalpha - a function that checks for alphabetic character
  * @c: int used for the function's argument
  * Return: 1 if c is a letter, lowercase or uppercase
  * Returns 0 otherwise
  */

int _isalpha(int c)
{
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
	{
		return (1);
	}
	else
		return (0);
}
