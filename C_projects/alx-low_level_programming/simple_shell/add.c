#include <stdio.h>
#include <unistd.h>

int main(void)
{
	int a = 6;
	int b = 9;
	int sum = a + b;
	pid_t pid;

	pid = getpid();

	printf("Sum is %d\n", sum);

	printf("PID is %u\n", pid);

	return 0;
}
