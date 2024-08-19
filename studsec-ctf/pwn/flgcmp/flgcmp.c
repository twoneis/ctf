#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int
main()
{
	FILE *fd;
	char input[80];
	char flag[80];

	fd = fopen("/flag.txt", "r");

	fgets(flag, 80, fd);

	printf("Whats the password?\n");

	if (fgets(input, 80, stdin) != NULL) {
		if (strcmp(input, flag) != 0) {
			printf(
			    "Incorrect flag, you have lost root privileges!\n");
			setuid(getuid()); // Drop privileges
		} else {
			printf("Welcome root\n");
		}

		char *args[] = { "sh", 0 };
		execvp("/bin/sh", args);
	}

	return 0;
}
