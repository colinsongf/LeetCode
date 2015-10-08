int removeElement(int *array,int size,int elem){
	if(size<=0)
		return size;
	int i,nextpos=0;
	for(i=0;i<size;++i)
		if(*(array+i)!=elem)
			*(array+nextpos++)=*(array+i);
	return nextpos;
}