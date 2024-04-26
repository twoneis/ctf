#!/bin/sh
clang-15 pwn.c -no-pie -fno-stack-protector -Os -std=c99 -o pwn