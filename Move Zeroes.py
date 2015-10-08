int bigerThan(int a, int b) {
	if (a == b)
		return 0;
	if (!a)
		return 1;
	return 0;
}

void moveZeroes(int *data, int numsSize) {
	if (!data || numsSize < 2)
		return ;
	int i, j, pivot;
	for (i = 1;i < numsSize; ++i) {
		pivot = data[i];
		for (j = i - 1;j >= 0 && bigerThan(data[j], pivot);--j)
			data[j + 1] = data[j];
		data[j + 1] = pivot;
	}
}