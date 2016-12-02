class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        vector<int> flags(nums.size());
        for (vector<int>::iterator it = flags.begin();it != flags.end(); ++it)
        {
            *it = -1;
        }
        for (int i = 0;i < nums.size(); ++i)
        {
            int flag = i;
            if (flags[i] != -1)
            {
                continue;
            }
            flags[i] = i;
            int current = i;
            int next = (nums.size() + current + nums[current]) % nums.size();
            bool forward = nums[current] >= 0? true: false;
            bool direction = true;
            while (current != next && flags[next] == -1 && direction)
            {
                flags[current] = i;
                current = next;
                if ((forward && nums[current] < 0) || (!forward && nums[current] > 0))
                {
                    direction = false;
                }
                next = (nums.size() + current + nums[current]) % nums.size();
            }
            if (current == next || !direction || flags[next] < i)
            {
                continue;
            }
            return true;
        }
        return false;
    }
};
