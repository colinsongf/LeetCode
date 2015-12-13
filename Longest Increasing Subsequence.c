#include <stdio.h>

int lengthOfLIS(int* nums, int numsSize) {
    if (!numsSize) {
        return 0;
    }
    int m[numsSize], i, j;
    int maxLength = 1;
    for (i = 0;i < numsSize; ++i) {
    	m[i] = 1;
    }
    for (i = 1;i < numsSize; ++i) {
    	for (j = 0;j < i; ++j) {
    		if (nums[j] < nums[i] && m[j] + 1 > m[i]) {
    			m[i] = m[j] + 1;
    		}
    	}
    	if (m[i] > maxLength) {
    		maxLength = m[i];
    	}
    }
    return maxLength;
}
