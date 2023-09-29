#include <stdio.h>

int main(void)
{
	int sz;
	printf("enter the size of the array ");
	scanf("%d", &sz);
	int arr[sz];
	int *p = arr;
	int *r = arr + sz;
	for (p = arr; p < arr + sz; p++)
	{
		printf("enter the value of arr[%d] = ", p - arr);
		scanf("%d", p);
	}
	
	for (p = arr , r = arr + sz - 1; p < r; p++,r--)
	{
		int tmp = *r;
		*r = *p;
		*p = tmp;
	}
	/* or you can use this :
	    
	   while (p < r)
   	    {
        	int tmp = *p;
        	*p = *r;
      	 	*r = tmp;

        	p++;
        	r--;
    	    }
	*/
	
	for (p = arr ; p < arr + sz; p++)
	{
		printf(" %d ", *p);
	}
	return 0;
}


