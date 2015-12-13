class Solution:
    def containsDuplicate(self, nums):
        size=len(nums)
        if size<=1:
            return False
        hashmap={}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num]=1
        return False
    def containsNearbyDuplicate(self,nums,k):
        size=len(nums)
        if not size:
            return False
        if k>=size-1:
            return self.containsDuplicate(nums)
        hashmap={}
        for i in range(k+1):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                return True
        i=k+1
        while i<size:
            #print hashmap
            headindex=i-1-k
            del hashmap[nums[headindex]]
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]]=1
            i+=1
        return False