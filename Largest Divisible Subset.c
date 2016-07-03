int cmp(const void *n1, const void *n2) {
    return *(int *)n1 - *(int *)n2;
}

int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {
    int *m = malloc(sizeof(int) * numsSize);
    int *record = malloc(sizeof(int) * numsSize);
    int *answer;
    int i, j, max, who;
    if (!nums || numsSize == 0) {
        return NULL;
    }
    qsort(nums, numsSize, sizeof(int), cmp);
    m[0] = 1;
    record[0] = -1;
    for (i = 1;i < numsSize; ++i) {
        m[i] = 1;
        record[i] = -1;
        for (j = i - 1;j >= 0; --j) {
            if (nums[i] % nums[j] == 0) {
                m[i] = m[j] + 1;
                record[i] = j;
                break;
            }
        }
    }
    //
    max = m[0];
    who = 0;
    for (i = 1;i < numsSize; ++i) {
        if (m[i] > max) {
            max = m[i];
            who = i;
        }
    }
    answer = malloc(sizeof(int) * max);
    j = max - 1;
    while (j >= 0 && who >= 0) {
        answer[j] = nums[who];
        j -= 1;
        who = record[who];
    }
    *returnSize = max;
    return answer;
}
