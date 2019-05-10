#!/bin/bash

CC=$1
EXENAME=$2
FLAGS="-o $EXENAME -O0 -g"

printf "CPP=$CC" > makefile
printf "CFLAGS=$FLAGS" >> makefile
printf "%.o: %.cpp\n    \$($CC) $FLAGS \$<" >> makefile
printf "$EXENAME:\n    \$($CC) $FLAGS \$($FLAGS)" >> makefile
