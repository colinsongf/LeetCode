void quickswap(int *data, int pos1, int pos2){
	if (pos1 == pos2)
		return ;
	*(data + pos1) ^= *(data + pos2);
	*(data + pos2) ^= *(data + pos1);
	*(data + pos1) ^= *(data + pos2);
}

int quicksplit(int *arr,int size,int k){
	int i = 0,j = size;
	while (i < j) {
		int p = i + 1;
		int q = j - 1;
		while (p <= q) {
			while (p <= q && arr[p] <= arr[i])
				p++;
			while (p <= q && arr[q] > arr[i])
				q--;
			if (p < q) {
				quickswap(arr, p, q);
				p++;
				q--;
			}
		}
		quickswap(arr, i, q);
		if (q == k) {
			return arr[q];
		} else if (q < k) {
			i = q + 1;
		} else {
			j = q;
		}
	}
	return -1;
}

int urRight(int *nums,int numsSize,int who){
	int counter = 0;
	int i;
	for(i = 0;i < numsSize;++i)
		if (nums[i] == who)
			counter++;
	return (counter > numsSize/3);
}

int* majorityElement(int* nums, int numsSize, int* returnSize) {
	if (! nums || ! numsSize) {
		*returnSize = 0;
		return malloc(sizeof(int));
	}
	if (numsSize == 1) {
		int o;
		int *answer = malloc(sizeof(int) * numsSize);
		*returnSize = numsSize;
		answer[0] = nums[0];
		return answer;
	}
	if (numsSize == 2){
		int o;
		if (nums[0] == nums[1])
			numsSize = 1;
		int *answer = malloc(sizeof(int) * numsSize);
		*returnSize = numsSize;
		for (o = 0;o < numsSize; ++o)
			answer[o] = nums[o];
		return answer;
	}
	int i = quicksplit(nums,numsSize,numsSize/3);//quicksplit_old(nums,0,numsSize,numsSize/3,numsSize);
	int j = quicksplit(nums,numsSize,numsSize*2/3);//quicksplit_old(nums,0,numsSize,numsSize*2/3,numsSize);
	int k;
	int tempAnswer[3],tempsize = 0;
	if (urRight(nums,numsSize,i))
		tempAnswer[tempsize++] = i;
	if (j != i && urRight(nums,numsSize,j))
		tempAnswer[tempsize++] = j;
	if (numsSize % 3) {
		k = quicksplit(nums,numsSize,numsSize);//quicksplit_old(nums,0,numsSize,2,numsSize);
		if (j != k && i != k && urRight(nums,numsSize,k))
			tempAnswer[tempsize++] = k;
	}
	*returnSize = tempsize;
	if (tempsize == 0)
		return malloc(sizeof(int));
	int *answer = malloc(sizeof(int) * tempsize);
	for(i = 0;i < tempsize;++i)
		answer[i] = tempAnswer[i];
	return answer;
}