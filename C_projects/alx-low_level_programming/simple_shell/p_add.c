#include <stdio.h>
#include <unistd.h>

int main(void)
{
	int a = 6;
	int b = 9;
	int sum = a + b;
	pid_t ppid;

	ppid = getppid();

	printf("Sum is %d\n", sum);

	printf("PPID is %u\n", ppid);

	return 0;
}
