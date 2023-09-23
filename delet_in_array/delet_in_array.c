#include <stdio.h>

int main(void)
{   
	int sz, ndx , q = 0, t;
	int arr[100];
	printf("enter the size of the array ");
	scanf("%d", &sz);
	printf("******************************************\n");

	do{
		printf("Enter the arr[%d] = ", q);
		scanf("%d", &arr[q]);
		q++;
	}while(q < sz);
	printf("******************************************\n");

	printf("Enter the index that you want to delet ");
	scanf("%d", &ndx);
	// 10 15 4 9 88
	for (int i = ndx; i < sz ; i++)
	{
		arr[i] = arr[i+1];
	}
	printf("******************************************\n");
	printf("This is the new array \n");
	for (int i = 0; i < sz - 1; i++)
	{
		printf("arr[%d] = %d\n", i, arr[i]);
	}
	return 0;
}
