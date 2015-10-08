int missingNumber(int* nums, int numsSize) {
    int summary = (1 + numsSize) * numsSize / 2;
    int i;
    for (i = 0;i < numsSize; ++i)
        summary -= nums[i];
    return summary;
}
/*
    0....n总和是(1 + n) * n / 2
    用总和 减去数组总和 = 没出现的那个值
*/