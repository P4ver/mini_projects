#include <stdio.h>

char *gago(char *arr, char del)
{	
	int y, i;
	int size = strlen(arr);
	
	for (i = 0; i < size; i++)
	{
		if (arr[i] == del)
		{
			for (y = i; y < size; y++)
				arr[y] = arr[y + 1];
			size--;
			i--;
		}
	}
	return arr;
}
int main(void)
{               
	char arr[20];
	char del;
	
	printf("enter the text ");
	gets(arr);
	
	printf("Enter the char that will be avoided ");
	scanf("%c", &del);
	
	printf("the text will be like %s", gago(arr, del));

	return 0;
}
