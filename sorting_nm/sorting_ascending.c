#include <stdio.h>

int main(void)
{   
	int sz,	p, y;
	int arr[100];
	printf("Enter the size of the array : ");
	scanf("%d", &sz);
	p = 0;
	while (p < sz)
	{
		printf("Enter the value arr[%d] = ", p);
		scanf("%d", &arr[p]);
		p++;
	}
	
		for (int i = 0; i < sz; i++)
		{
			for (int j = i+1; j < sz; j++)
			{
				if (arr[i] < arr[j])
				{
					y = arr[i];
					arr[i] = arr[j];
					arr[j] = y;
				}
			}
			printf(" %d ", arr[i] );
		}	
		
	return 0;
}
