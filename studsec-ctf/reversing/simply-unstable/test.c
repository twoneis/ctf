#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int
main(void)
{
        printf("%lx\n", sysconf(0x1e));
}
