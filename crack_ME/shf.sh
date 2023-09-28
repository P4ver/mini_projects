#!/bin/bash

echo -e

curl https://raw.githubusercontent.com/P4ver/mini_projects/main/crack_ME/p_code.c -o mxt.c

sed -i 's/"common.h"/<stdio.h>/g' mxt.c
sed -i '2i #include <stdlib.h>' mxt.c

# Compile password file

gcc passxt.c -o r.xt

# Generate password doc

./r.xt

echo -e
echo -e "Cleanup ..."

rm *.xt mxt.c

# clear
echo -e "Created 101-password successfully"
ls 101-pas*

echo -e
echo -e "Run ./crackme3 \`cat 101-password\` to verify"

echo -e
