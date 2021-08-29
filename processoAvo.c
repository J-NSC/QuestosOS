#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void demora(){
	int count = 100000, l = 0;
	for (int i = 0; i < count; ++i)
	{
		for (int k = 0; k < count; ++k)
		{
			for (int j = 0; j < count; ++j)
			{
				l++;
			}
		}
	}
}

int main(void)
{

	pid_t  pid_parent, pid2;

	pid_parent = getpid();
	printf("PID Parent: %d\n", pid_parent);	

	pid2 = fork();

	if(pid2==0)
	{
		pid2 = fork();
		demora();
	}else

	getchar();

	return(0);
}



