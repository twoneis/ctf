#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char password[16];
unsigned char logged_in;

int main(int argc, char **argv)
{
    logged_in = 0;

    //Show where password and logged_in are located in memory
    printf("password  @ %p\n", &password[0]);
    printf("logged_in @ %p\n", &logged_in);

    //Read the password
    printf("Enter password: ");
    fflush(stdout);
    gets(password);

    //If the password is equal to the expected one, set logged_in to 1/true
    //Note: the correct password is not REDACTED !
    if(strcmp(password, "REDACTED") == 0) {
        logged_in = 1;
    }

    if(logged_in) {
        printf("Correct password!\n");
        //Note: the correct flag is not flag{REDACTED} !
        printf("Flag: flag{REDACTED}\n");
    }
    else {
        printf("Wrong password!\n");
    }

    return 0;
}
