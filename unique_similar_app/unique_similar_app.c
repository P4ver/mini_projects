#include <stdio.h>

int main(void)
{   
	int sz, uniq, select;
	int arr[100];

	printf("Choose the app :\n  1- unique numbers \t 2- similar numbers\n");
	scanf("%d", &select);
	if (select == 1)
	{
		printf ("This app selects unique numbers\n");
		printf("**********************************\n");
		printf ("Enter the size of the array : ");
		scanf("%d", &sz);
		printf("**********************************\n");
		for (int i = 0; i < sz; i++)
		{
			printf("Enter the values of the array arr[%d] = ", i);
			scanf("%d", &arr[i]);
		}
		printf("**********************************\n");
		for (int i = 0; i < sz; i++)
		{
			uniq = 1;
			for (int j = 0; j < sz; j++)
			{
				if (arr[i] == arr[j] && i != j)
					uniq = 0;
			}
			if (uniq == 1)
				printf("*** arr[%d] = %d\n", i, arr[i]);
		}
	}
	else if (select == 2)
	{
		printf ("This app selects similar numbers\n");
		printf("***********************************\n");
		printf ("Enter the size of the array : ");
		scanf("%d", &sz);
		printf("***********************************\n");
		for (int i = 0; i < sz; i++)
		{
			printf("Enter the values of the array arr[%d] = ", i);
			scanf("%d", &arr[i]);
		}
		printf("***********************************\n");
		for (int i = 0; i < sz; i++)
		{
			uniq = 1;
			for (int j = 0; j < sz; j++)
			{
				if (arr[i] == arr[j] && i != j)
					uniq = 0;
			}
			if (uniq == 0)
				printf("*** arr[%d] = %d\n", i, arr[i]);
		}		
	}
	else
		printf(" You typed the wrong the number ");
	return 0;
}
