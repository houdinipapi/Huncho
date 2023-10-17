#include <stdio.h>
#include <unistd.h>

int main(void)
{
	int a = 9;
	int b = 3;
	int diff = a - b;

	pid_t ppid;

	ppid = getppid();

	printf("Difference is %d\n", diff);

	printf("PPID is %u\n", ppid);

	return 0;
}
