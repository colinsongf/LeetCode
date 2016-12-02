int minMoves(int* nums, int numsSize) {
    //finally, every num in nums = cell
    //cell * numsSize = sum + (cell - min) * (numsSize - 1) ---> cell = sum - numsSize * min + min
    //step = cell - min = sum - numsSize * min + min - min = sum - numsSize * min
    int i, sum = 0, min = INT_MAX, step;
    for (i = 0;i < numsSize; ++i)
    {
        if (nums[i] < min)
        {
            min = nums[i];
        }
        sum += nums[i];
    }
    step = sum - numsSize * min;
    return step;
}
