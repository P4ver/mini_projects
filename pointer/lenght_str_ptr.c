#include <stdio.h>
#include <string.h>

int main(void)
{
	int sz;
	char nam[100] = "mohammed habti";
	
	char *p = nam;

	int n = 0;
	
	while (*p != '\0')
 	{
		printf("%c", *p);
		p++;
		n++;
	}
	printf("\n the lenght of the string is %d",n);
	
	return 0;
}
