class Solution {
public:
    int thirdMax(vector<int>& nums0) {
        set<int> st;
        for (int i = 0;i < nums0.size(); ++i)
        {
            st.insert(nums0[i]);
        }
        vector<int> nums;
        for (set<int>::iterator it = st.begin(); it != st.end(); ++it)
        {
            nums.push_back(*it);
        }
        if (nums.size() == 1)
        {
            return nums[0];
        }
        if (nums.size() == 2)
        {
            return nums[0] > nums[1]? nums[0]: nums[1];
        }
        int big, mid, small;
        if (nums[0] >= nums[1] && nums[0] >= nums[2])
        {
            big = nums[0];
            if (nums[1] > nums[2])
            {
                mid = nums[1];
                small = nums[2];
            }
            else
            {
                mid = nums[2];
                small = nums[1];
            }
        }
        else if (nums[1] >= nums[0] && nums[1] >= nums[2])
        {
            big = nums[1];
            if (nums[0] > nums[2])
            {
                mid = nums[0];
                small = nums[2];
            }
            else
            {
                mid = nums[2];
                small = nums[0];
            }
        }
        else
        {
            big = nums[2];
            if (nums[0] > nums[1])
            {
                mid = nums[0];
                small = nums[1];
            }
            else
            {
                mid = nums[1];
                small = nums[0];
            }
        }
        for (int i = 3;i < nums.size(); ++i)
        {
            if (nums[i] >= big)
            {
                small = mid;
                mid = big;
                big = nums[i];
            }
            else if (nums[i] >= mid)
            {
                small = mid;
                mid = nums[i];
            }
            else if (nums[i] >= small)
            {
                small = nums[i];
            }
        }
        return small;
    }
};
