#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>


int main (){

	pid_t pid, pid2;
	char syscall[11];

	pid = getpid();
	printf("PID parent: %d\n",pid );
	pid2 = fork();

	if(pid2 != 0){
		pid2 =fork();
	}


	getchar();

	return 0;
}