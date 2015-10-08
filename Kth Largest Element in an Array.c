void swap(int *data,int pos1,int pos2){
	int t=*(data+pos1);
	*(data+pos1)=*(data+pos2);
	*(data+pos2)=t;
}

int quicksplit(int *data,int head,int rear,int size,int k){
	if(head>=rear)
		exit(1);
	int pivot=*(data+head);
	int firstbig=head+1;
	int i;
	for(i=head+1;i<rear;++i)
		if(*(data+i) < pivot)
			swap(data,i,firstbig++);
	swap(data,head,firstbig-1);
	//firstbig-1
	if(firstbig-1 == size-k)
		return *(data+firstbig-1);
	else if(firstbig-1 > size-k)
		return quicksplit(data,head,firstbig-1,size,k);
	else
		return quicksplit(data,firstbig,rear,size,k);
}

int findKthLargest(int* nums, int numsSize, int k){
	return quicksplit(nums,0,numsSize,numsSize,k);
}