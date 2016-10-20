class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (!nums.size())
        {
            return 0;
        }
        vector<int> up(nums.size());
        vector<int> down(nums.size());
        //init
        up[0] = down[0] = 1;
        //dynamic
        for (int i = 1;i < nums.size(); ++i)
        {
            int num = nums[i];
            //assign for up[i]
            up[i] = up[i - 1];
            for (int j = 0;j < i; ++j)
            {
                if (nums[j] < num && down[j] + 1 > up[i])
                {
                    up[i] = down[j] + 1;
                }
            }
            //assign for down[i]
            down[i] = down[i - 1];
            for (int j = 0;j < i; ++j)
            {
                if (nums[j] > num && up[j] + 1 > up[i])
                {
                    down[i] = up[j] + 1;
                }
            }
        }
        return max(up.back(), down.back());
    }
};
