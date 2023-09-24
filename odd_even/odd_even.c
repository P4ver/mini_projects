#include <stdio.h>

int main(void)
{   
	int sz,	pair, y;
	int arr[100]= {1,6,4,3,2,5};
	int even[50];
	int odd[50];
    y = 0;
	int x = 0;
	
	printf("enter the size of the array ");
	scanf("%d", &sz);
	printf("**********************************\n");
	for (int i = 0; i < sz; i++)
	{
		printf("Enter the value the array arr[%d] : ", i);
		scanf("%d", &arr[i]);
	}
	printf("**********************************\n");
	for (int i = 0; i < sz; i++)
	{
		if (arr[i] % 2 == 0)
		{
			even[y] = arr[i];
			printf("even[%d] = %d \n", y,even[y]);
			y++;
		}
		else
		{
			odd[x] = arr[i]; 
			x++;
		}
		 pair = sz - y;;
	}
	for (int l = 0; l < pair; l++)
		printf("odd[%d] = %d \n", l, odd[l]);
	return 0;
}
