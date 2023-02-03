#include <stdio.h>
#include <string.h>

/**
 * main - concatenating string
 */

void main(void)
{
	char country[20];
	char city[10];
	int l_country, l_city, i;

	printf("Enter a country: ");
	gets(country);
	printf("Enter a city: ");
	gets(city);

	l_country = strlen(country);
	l_city = strlen(city);

	for (i = 0; i <= l_city; i++)
	{
		country[l_country + i] = city[i];
	}

	printf("The new string is: %s\n", country);
}
