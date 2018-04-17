
#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h> 
void *fun1();
void *fun2();
int a[2]={1,2};
int r,rv,tcm=10;                     //here tcm is total no of cats and mice
int v,cv;
int w,mv;
int numcats[5]={1,2,3,4,5}; 
int nummice[5]={1,2,3,4,5};                     
pthread_mutex_t l;
int main()
{
	int i;
	
	pthread_t c,m;
	pthread_mutex_init(&l,NULL);
	
	for(i=0;i<tcm;i++)
	{
		r=rand()%2;
		rv=a[r];
		printf("%d\n",rv);
	    	if (rv==1)
		{
			w=rand()%5;
			mv=nummice[w];
			printf("cat is not present so mice %d is  eating\n\n",mv);
			sleep(1);
		}         
	    	else
		{
			v=rand()%5;
			cv=numcats[v];
			printf("cat %d is eating\n\n",cv);
			r=rand()%2;
			rv=a[r];
			if(rv==1)
			{
				pthread_create(&c,NULL,fun1,NULL);
				pthread_join(c,NULL);
				sleep(2);
			}
			else
			{
				pthread_create(&m,NULL,fun2,NULL);
				pthread_join(m,NULL);
				sleep(2);	
			}
		}
	}
}
void *fun1()
{
	w=rand()%5;
	mv=nummice[w];
	printf("mice is very hungry somice %d attempts to eat snacks of cat:\n\n",mv);
	r=rand()%2;
	rv=a[r];
	printf("%d\n",rv);
    	if (rv==1)
	{
		printf("mice was too fast to catch cat %d is out of the group\n\n",cv);
		
	}         
    	else
	{
		printf("cat eating mouse\n\n");
	}
	return 0;	
}
void *fun2()
{
	pthread_mutex_lock(&l);
	printf("mice is afraid to come to eat cats snacks bez cat is eating:\n\n");
	pthread_mutex_unlock(&l);	
}
