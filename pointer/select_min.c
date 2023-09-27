#include <stdio.h>
    
int main(void)
{              
	int arr[5];
	int *p = arr;
	int min;
	
	for (p = arr; p < arr + 5; p++)
	{
		printf("enter the value of the arr[%d]= ",p-arr);
		scanf("%d", p);
	}
	/*first way:
	p = arr;
	min = *p;
	second way:
	min = *arr;
	*/
	min = arr[0];

	for (p = arr; p < arr + 5; p++)
	{
		if (*p < min)
			min = *p;
	}
	printf("the min is %d", min);
	return 0;
} 
