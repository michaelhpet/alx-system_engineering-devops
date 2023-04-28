#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <sys/types.h>

int infinite_while(void);

/**
 * main - create 5 zombie processes
 * Return: 0 if success, non-zero otherwise
 */
int main(void)
{
	pid_t pid;
	char i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
			exit(EXIT_FAILURE);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}

/**
 * infinite_while - wait for infinity
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
