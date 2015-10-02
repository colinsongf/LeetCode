#include <stdio.h>

int removeDuplicates(int *array,int size){
	if(size<=1)
		return size;
	int prev=*array,i;
	int nextpos=1,counter=1;
	for(i=1;i<size;++i)
		if(*(array+i)!=prev){
			prev=*(array+i);
			counter=1;
			*(array+nextpos++)=*(array+i);
		}else if(counter<2){
			*(array+nextpos++)=*(array+i);
			counter++;
		}
	return nextpos;
}

int main(){
	int array[]={1,1,1,2,2,3},size=sizeof array/sizeof *array;
	int newsize;
	printf("%d\n",newsize=removeDuplicates(array,size));
	for(int i=0;i<newsize;++i)
		printf("%d ",array[i]);
	printf("\n");
}
