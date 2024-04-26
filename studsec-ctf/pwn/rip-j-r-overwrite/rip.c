#include <stdio.h>
#include <unistd.h>

//Your goal is to execute the print_flag function!
void print_flag()
{
    printf("flag{REDACTED}\n");
}

int main()
{
    char name[16];

    //Hint: print where print_flag is located in memory (i.e. where you should jump)
    printf("print_flag @ %p\n", &print_flag);

    //Read a string
    printf("Please enter your name: ");

    gets(name);

    //Print introduced name
    printf("Howdy %s !\n", name);

    //Hint: show where the main function will return
    printf("main has ended! Returning to %p\n", __builtin_return_address(0));
    return 0;
}
