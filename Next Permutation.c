void swapArr(int *nums,int i,int j){
	int t = nums[i];
	nums[i] = nums[j];
	nums[j] = t;
}

void reverseArr(int *nums,int head,int rear){
	while (head < rear) 
		swapArr(nums,head++,rear--);
}

void nextPermutation(int* nums, int numsSize) {	
	int i,j;
	for (i = numsSize - 2;i >= 0; --i)
		if (nums[i] < nums[i + 1])
			break;
	if (i == -1)
	{
		reverseArr(nums,0,numsSize - 1);
		return ;
	}
	for (j = numsSize - 1; j > i; --j)
		if (nums[i] < nums[j])
			break;
	swapArr(nums,i,j);
	reverseArr(nums,i + 1,numsSize - 1);
}