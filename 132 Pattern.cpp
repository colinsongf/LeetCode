class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int min = INT_MIN;
        stack<int> mystack;
        for (vector<int>::reverse_iterator it = nums.rbegin();it != nums.rend(); ++it)
        {
            if (*it < min)
            {
                return true;
            }
            else
            {
                while (!mystack.empty() && mystack.top() < *it)
                {
                    min = mystack.top();
                    mystack.pop();
                }
                mystack.push(*it);
            }
        }
        return false;
    }
};
