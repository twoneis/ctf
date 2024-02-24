#include <unistd.h>
#include <stdio.h>

int
main(void)
{
        printf("%li\n", sysconf(0x01));
        return 0;
}
