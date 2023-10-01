#include <stdio.h>
#include <string.h>

int main(void)
{
	int sz;
	char nam[100] = "mohammed";

	int i = 0, j = 0, u;
	int max_c = 0;
	char mstchar;

	for (i = 0; i < 10; i++)
	{
		u = 1;
        	for (j = i + 1; j < 10; j++)
        	{
            		if (nam[i] == nam[j])
            		{
                		printf("%c ", nam[i]);
                		u++; 
            		}
        	}
		if (u > max_c)
		{
			max_c = u;
			mstchar = nam[i];
		}
	}
	printf("the most repeat %c ", mstchar);
	return 0;
}

/**
 * with pointers

#include <stdio.h>
#include <string.h>

int main(void)
{
    char nam[10] = "mohammed";
    int length = strlen(nam);

    char mostRepeatedChar;
    int maxCount = 0;

    for (char *ptr = nam; *ptr != '\0'; ptr++)
    {
        int count = 1;
	for (char *innerPtr = ptr + 1; *innerPtr != '\0'; innerPtr++)
        {
            if (*ptr == *innerPtr)
            {
                count++;
            }
        }

        if (count > maxCount)
        {
            maxCount = count;
            mostRepeatedChar = *ptr;
        }
    }

    printf("The most repeated character is '%c' with %d occurrences.\n", mostRepeatedChar, maxCount);

    return 0;
}
*/
