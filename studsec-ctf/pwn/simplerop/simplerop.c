#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool authenticated = false;

void login(int username, int password)
{
    if(username == 0xdeadbeef && password == 0xcafebabe) {
        authenticated = true;
    }
}

void print_flag(bool printFlag)
{
    if(printFlag) {
        if(authenticated) {
            puts("Well done, here is your flag:");
            FILE* fh = fopen("flag.txt", "r");
            char c;
            c = fgetc(fh);
            while (EOF != c && printFlag && authenticated) {
                printf("%c", c);
                c = fgetc(fh);
            }
            fclose(fh);
        }
        else {
            puts("You are not authenticated");
        }
    }
    else {
        puts("No flag for you!");
    }
}

// TODO: make this function useful
void get_input() {
    char buf[100];

    scanf("%s", buf);
}

int main()
{
    get_input();
    print_flag(false);

    return 0;
}
