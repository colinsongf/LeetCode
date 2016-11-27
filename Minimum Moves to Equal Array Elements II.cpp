class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int answer = 0;
        if (nums.empty())
        {
            return answer;
        }
        sort(nums.begin(), nums.end());
        int tnum = nums[nums.size() / 2];
        int temp;
        for (vector<int>::iterator it = nums.begin();it != nums.end(); ++it)
        {
            answer += *it <= tnum? tnum - *it: *it - tnum;
        }
        return answer;
    }
};
