CC = gcc
CFLAGS = -Wall -Wextra -Werror

all: stackscript

stackscript: setup.c
	$(CC) $(CFLAGS) -o stackscript setup.c

clean:
	rm -f stackscript
