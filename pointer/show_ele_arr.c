#include <stdio.h>

int main(void)
{
	int ar[100];
	int sz;
	int *p = ar;
	
	printf("enter the size of the array ");
	scanf("%d", &sz);
	printf("*********************************\n");
	for (p = ar; p < ar + sz; p++)
	{
		printf("enter the value of arr[%d] = ", p - ar);
		scanf("%d", p);
	}
	printf("*********************************\n");	
	for (p = ar; p < ar + sz; p++)
	{
		printf("arr[%d]\n", *p);
	}
	
	return 0;
}
