#include <stdio.h>
#include <unistd.h>

int main(void)
{
	pid_t pid;
	pid_t ppid;

	// printf("Before fork I was one\n");

	pid = fork();

	if (pid == -1)
	{
		perror("Unsuccessful\n");
		return 1;
	}

	if (pid == 0)
	{
		sleep(40);
		printf("I am the child\n");
	}
	else
	{
		ppid = getpid();
		printf("Parent PID is %u\n", ppid);
	}

	// printf("After fork I became two\n");

	return 0;
}
