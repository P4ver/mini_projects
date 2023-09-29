#include <stdio.h>

int main(void)
{
	int arr[5] ={12,9,68,7,9};
	int *p = arr;
	int *r = arr;

	for (p = arr; p < arr + 5; p++)
	{
		*r = *p;
		if (*r != 9)
			r++;
		/**
		 * you can use this :
		 * if (*r != 9)
		 * {
		 *	*r = *p;
		 *	r++;
		 * }
		 */
	}
	for (p = arr; p < r; p++)
		printf("%d ", *p);
	return 0;
}

