#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void print_usage() {
    printf("Usage: ./stackscript stsc_program_path\n");
}

void call_stsc_interpreter(char python_cmd[1024], char program_path[1024]) {
    char command[1024];
    snprintf(command, sizeof(command), "%s ./src/stackscript.py %s", python_cmd, program_path);
    system(command);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Please provide the path to the stsc program.\n");
        print_usage();
        return 1;
    }
    // on some machines, python3 is not found and python must be called instead.
    char python_cmd[1024];
    if (system("command -v python3 >/dev/null 2>&1") == 0) {
        strcpy(python_cmd, "python3");
    } else {
        strcpy(python_cmd, "python");
    }
    call_stsc_interpreter(python_cmd, argv[1]);
    return 0;
}
