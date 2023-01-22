#include <stdio.h>

/**
 * main - main function
 */

char get_name(char username[30]);

int main(void)
{
	char username[30];
	
	username[30] = get_name("Enter your name: ");
}

char get_name(char username[30])
{
	//printf("What is your name? "\n);
	scanf("%s", username);
}
