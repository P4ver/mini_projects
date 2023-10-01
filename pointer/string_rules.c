int main(void)
{
	char str[6]={'h','a','b','t','i','\0'};
	char test[50];//you should fill between the square brackets
	char txt[]= "mohammed habti";//best way to write string
	char *string = "morocco";//string cte
	
	char *ptr = txt;
	printf("%s\n", ptr + 3);
	
	for (int i = 0; i < 5; i++)
	{
		printf("%c", str[i] );
		printf("\n");
	}
	
	printf("%s\n", txt);
	
	for (int i = 0; i < 14; i++)
		printf("%c", txt[i]);
	
	printf("\n");
	int i = 0;
	
	while (i < 7)
	{	
		printf("%c", *string);
		string++;
		i++;
	}
	printf("\n");
	char name[50];
	printf("enter your name ");
	gets(name);
	// printf("your name is %.8s", name);
	
	char *j = strstr(txt,"hab");
	printf("%s\n", j);
	
	int l = strlen(txt);
	printf("=> %d\n", l);
	
	return 0;
	
}
