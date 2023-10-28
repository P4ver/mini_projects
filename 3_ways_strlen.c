#include <stdio.h>

int _strlen(char *s)
{
	int lenghtS = 0;
	
	while (*(s + lenghtS) != '\0')
		lenghtS++;
	/*
	while (s[lenghtS] != '\0')
		lenghtS++;
	
	while (*s != '\0')
	{
		lenghtS++;
		s++;
	}
	*/
	return (lenghtS);
}

int main(void)
{
    char *str;
    int len;

    str = "My first strlen!";
    len = _strlen(str);
    printf("%d\n", len);
    return (0);
}
