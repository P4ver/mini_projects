#!/bin/bash

curl https://raw.githubusercontent.com/P4ver/mini_projects/main/crack_ME/p_code.c -o mxt.c

sed -i 's/"common.h"/<stdio.h>/g' mxt.c
sed -i '2i #include <stdlib.h>' mxt.c

gcc mxt.c -o r.xt

./r.xt

rm *.xt mxt.c

ls 101-pas*
