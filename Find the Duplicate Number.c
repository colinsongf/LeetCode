int findDuplicate(int* nums, int numsSize) {
    int i, t;
    for (i = 0;i < numsSize; ++i) {
        while (nums[i] != i + 1) {
            t = nums[nums[i] - 1];
            if (t == nums[i])
                return t;
            nums[nums[i] - 1] = nums[i];
            nums[i] = t;
        }
    }
    return -1;
}