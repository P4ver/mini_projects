#include <stdio.h>


void rev_string(char *s)
{
	char rev;
	int y = 0;
	int q;
	
	while (s[y] != '\0')    /* or *(s + y) != '\0' */
	{
		y++;
	}

	for (q = 0; q < y; q++)
	{
		y--;
		rev = *(s + q); /*or  rev = s[q] they are the same*/
		*(s + q) = *(s + y);
		*(s + y) = rev;
	}
}

int main(void)
{
    char s[10] = "My School";

    printf("%s\n", s);
    rev_string(s);
    printf("%s\n", s);
    return (0);
}

