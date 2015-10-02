#include <stdio.h>

int removeDuplicates(int *array,int size){
	if(size<=1)
		return size;
	int prev=*array,i;
	int nextpos=1;
	for(i=1;i<size;++i)
		if(*(array+i)!=prev){
			prev=*(array+i);
			*(array+nextpos++)=*(array+i);
		}
	return nextpos;
}

int main(){
	int array[]={1,1,2},size=sizeof array/sizeof *array;
	int newsize;
	printf("%d\n",newsize=removeDuplicates(array,size));
	for(int i=0;i<newsize;++i)
		printf("%d ",array[i]);
	printf("\n");
}
