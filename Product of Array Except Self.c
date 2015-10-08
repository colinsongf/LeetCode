/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *answer = malloc(sizeof(int) * numsSize);
    int head[numsSize],rear[numsSize];
    int i;
    head[0] = nums[0],rear[numsSize - 1] = nums[numsSize - 1];
    for (i = 1;i < numsSize; ++i)
        head[i] = head[i - 1] * nums[i];
    for (i = numsSize - 2;i >= 0; --i)
        rear[i] = rear[i + 1] * nums[i];
    for (i = 0;i < numsSize; ++i) {
        if (i == 0)
            answer[0] = rear[1];
        else if (i == numsSize - 1)
            answer[numsSize - 1] = head[numsSize - 2];
        else
            answer[i] = head[i - 1] * rear[i + 1];
    }
    *returnSize = numsSize;
    return answer;
}