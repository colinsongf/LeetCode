void swap(int* p, int* q)
{
    int t=*p; *p=*q; *q=t;
}

void sort(int* nums, int begin, int end)
{
    int l=begin, r=end;
    int v = nums[l+(r-l)/2];
    while(l <= r)
    {
        while(nums[l] < v) l++;
        while(nums[r] > v) r--;
        if(l <= r)
        {
            swap(nums+l, nums+r);
            l++; r--;
        }
    }
    if(begin < r)
        sort(nums, begin, r);
    if(l < end)
        sort(nums, l, end);
}

//AC - 40ms;
void wiggleSort(int* nums, int size)
{
    sort(nums, 0, size-1); //using quick sort to sort the array first;
    int *arr = (int*)malloc(sizeof(int)*size);
    for(int i = 0; i < size; i++)
        arr[i] = nums[i];
    int small= 0; //the first of smallers;
    int big = (size-1)/2+1; //the first of biggers;
    int index = size-1; //start to fill in reverse direction: from right to left;
    if(size%2 == 0) //if the size is even then the last should be indexed by odd size-1, so place the bigger one in odd position size-1;
        nums[index--] = arr[big++];
    while(index > -1)
    {
        nums[index--] = arr[small++];
        if(index > -1) //in case of "underflow";
            nums[index--] = arr[big++];
    }
}
