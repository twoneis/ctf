#include <stdio.h>

int
main()
{
	int a = 0xf;
	int b = 0xe;
	int c = (0xf + 0xe) << 1;
	printf("%i\n%i\n%i\n", a, b, c);
	return 0;
}
