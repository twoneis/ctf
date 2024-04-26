#!/bin/sh
clang-15 rip.c -no-pie -fno-stack-protector -Os -std=c99 -o rip