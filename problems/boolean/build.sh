#!/bin/bash
# first you have to build dynamic library from boolean.c file
# gcc -c -fPIC boolean.c -o boolean.o
# gcc -shared -Wl,-soname,libboolean.so -o libboolean.so boolean.o

gcc -c -fPIC bool1.c -o bool1.o
gcc -shared -Wl,-soname,libbool1.so -o libbool1.so bool1.o
