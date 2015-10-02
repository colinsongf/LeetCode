#include <stdio.h>

int removeElement(int *array,int size,int elem){
	if(size<=0)
		return size;
	int i,nextpos=0;
	for(i=0;i<size;++i)
		if(*(array+i)!=elem)
			*(array+nextpos++)=*(array+i);
	return nextpos;
}

int main(){
	int array[]={1,1,2},size=sizeof array/sizeof *array;
	int newsize;
	printf("%d\n",newsize=removeElement(array,size,1));
	for(int i=0;i<newsize;++i)
		printf("%d ",array[i]);
	printf("\n");
}
