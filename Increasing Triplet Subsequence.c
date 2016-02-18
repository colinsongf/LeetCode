#include <stdio.h>

int increasingTriplet(int *nums, int numsSize) {
    int small0 = INT_MAX, small1 = INT_MAX, i;
    for (i = 0;i < numsSize; ++i) {
        if (nums[i] <= small0) {
            small0 = nums[i];
        } else if (nums[i] <= small1) {
            small1 = nums[i];
        } else if (nums[i] > small0 && nums[i] > small1) {
            return true;
        }
    }
    return false;
}
