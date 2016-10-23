class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        long long offset=0,subsum=0;
        multiset<long long> ms;
        for(int i=0;i<nums.size();i++){
            offset-=nums[i];
            ms.insert(nums[i]+offset);
            auto itlow=ms.lower_bound(lower+offset),itup=ms.upper_bound(upper+offset);
            subsum+=distance(itlow,itup);
        }
        return (int)(subsum);
    }
};
