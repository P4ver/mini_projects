#include <stdio.h>

int main(void)
{   
	int sz, ndx, d = 0, t;
	int arr[50];
	
	printf("enter the the size of the array ");
	scanf("%d", &sz);
	
	printf("****************************************\n");
	do
	{
		printf("enter the values of the array ");
		scanf("%d", &arr[d]);
		d++;
	}while (d < sz);
	
	printf("****************************************\n");
	
	printf("enter the index to insert from (0 to %d) : ", sz - 1);
	scanf("%d", &ndx);
	
	printf("****************************************\n");
	
	printf("enter the value that will be inserted into the array ");
	scanf("%d", &t);
	
	for (int y = sz; y >= ndx ; y--)
	{
		arr[y] = arr[y - 1];
	}
	
	printf("****************************************\n");
	printf ("The new array with insertion : \n");
	arr[ndx] = t;
	for (int h = 0; h <= sz; h++)
	{
		printf(" %d ", arr[h]);
	}
	
	return 0;
}
