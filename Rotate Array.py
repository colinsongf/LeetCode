class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        size=len(nums)
        if k>size:
            k%=size
        nums[(-1)*k:]=reversed(nums[(-1)*k:])
        nums[:(-1)*k]=reversed(nums[:(-1)*k])
        nums.reverse()
        return nums       