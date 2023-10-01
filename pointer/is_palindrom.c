#include <stdio.h>
#include <string.h>

int main(void)
{
	int sz;
	char nam[100] = "kayak";

	char *p = nam;
	int i = 0, j = 0, u = 0;
	int len = strlen(nam);
	char *d = nam + len - 1;
	int ispa = 0;
	
	for (i = 0; i < len / 2; i++)
	{
		 if (nam[i] == nam[len - i - 1])
		 {
			printf("%c  %c\n", nam[i], nam[len - i- 1]);
			ispa = 1;
		 }
	}
	if (ispa)
		printf("the string is palindrom");
	
	return 0;
}
