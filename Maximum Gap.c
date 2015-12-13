#include <stdio.h>

void displayoutcome(int *data,int size){
	for(int i=0;i<size;i++)
		printf("%d ",*(data+i));
	printf("\n");
}

int getPos(int number,int pos){
	int divi=1,i;
	for(i=1;i<pos;i++)
		divi*=10;
	return (number/divi)%10;
}

void counterSort(int *data,int size,int bit){
	int counter[10]={},i,pos,tmpdata[size];
	for(i=0;i<size;i++)
		*(tmpdata+i)=*(data+i);
	for(i=0;i<size;i++)
		counter[getPos(data[i],bit)]++;
	for(i=1;i<10;i++)
		counter[i]+=counter[i-1];
	for(i=size-1;i>=0;i--){
		pos=--counter[getPos(tmpdata[i],bit)];
		data[pos]=tmpdata[i];
	}
}

void radixSort(int *data,int size){
	for(int bit=1;bit<=10;bit++)
		counterSort(data,size,bit);
}

int maximumGap(int *data,int size){
	radixSort(data,size);
	if(size<2)
		return 0;
	int maxdiff=data[1]-data[0];
	for(int i=2;i<size;i++)
		if(data[i]-data[i-1]>maxdiff)
			maxdiff=data[i]-data[i-1];
	return maxdiff;
}