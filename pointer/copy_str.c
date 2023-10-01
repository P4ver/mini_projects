#include <stdio.h>

int main(void)
{
	char arr[50];
	char bar[50];
	int i;
	printf("enter the string ");
	gets(arr);

	for (i= 0; arr[i] != '\0'; i++)
	{
		bar[i] = arr[i];
	}
	bar[i] = '\0';
	printf("\n%s", bar);
	
	return 0;
}
