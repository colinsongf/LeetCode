int rob_no_circle(int* nums, int head,int end) {
    int numsSize=end-head+1;
    if(numsSize==0)
        return 0;
    nums+=head;
    if(numsSize==1)
        return *nums;
    if(numsSize==2)
        return *nums > *(nums+1)?*nums:*(nums+1);
    int m[numsSize],i;
    m[0]=*nums;
    m[1]=*(nums+1);
    m[2]=*(nums+2)+m[0];
    for(i=3;i<numsSize;++i)
        m[i]=nums[i]+(m[i-3]>m[i-2]?m[i-3]:m[i-2]);
    return (m[numsSize-1]>m[numsSize-2]?m[numsSize-1]:m[numsSize-2]);
}

int rob(int* nums, int numsSize) {
    if(numsSize==0)
        return 0;
    if(numsSize==1)
        return *nums;
    if(numsSize==2)
        return *nums > *(nums+1)?*nums:*(nums+1);
    int max1=rob_no_circle(nums,0,numsSize-2);
    int max2=rob_no_circle(nums,1,numsSize-1);
    return max1>max2?max1:max2;
}