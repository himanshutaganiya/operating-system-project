#include<stdio.h>
#include<stdlib.h>
int n;
int tforct=0;
int comp (const void * elem1, const void * elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}
 
void calculation(int a[],int b[])
{
int tat[n],ct[n],x[n];
for(int i=0;i<n;i++)
{
x[i]=a[i];
}
qsort(x, sizeof(x)/sizeof(*x), sizeof(*x), comp);
for(int i=0;i<n;i++)
{
printf("elements are \n");
printf("%d\n",x[i]);
}
	for(int i=0;i<n;i++)
	{
	int j=search(x[i],a);
printf("index are\n");
printf("%d",j);
	ct[j]=tforct+b[j];
printf("ct is \n",ct[j]);
	tforct=ct[j];
	tat[j]=ct[j]-a[j];
        }
	display(ct,tat);
}

int search(int x,int a[])
{
for(int i=0;i<n;i++)
{
if(a[i]==x)
return i;
}
}


void display(int ct[],int tat[])
{
printf("Completion time  and turnaround time \n");
for(int i=0;i<n;i++)
{
printf("%d\t",ct[i]);
printf("%d\n",tat[i]);
}
}
int main()
{
printf("Enter the no of process\n");
scanf("%d",&n);
int a[n],b[n];
for(int i=0;i<n;i++)
{
scanf("%d",&a[i]);
scanf("%d",&b[i]);
}

calculation(a,b);
return 0;
}
