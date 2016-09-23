class Solution {
public:
    Solution(vector<int> nums):numbers(nums) 
    {
        srand(time(NULL));
    }
    
    int pick(int target) {
        int fm = 1;
        int select;
        int i;
        for (i = 0;i < numbers.size(); ++i)
        {
            if (numbers[i] == target)
            {
                int r = rand() % fm++;
                if (r < 1)
                {
                    select = i;
                }
            }
        }
        return select;
    }
private:
    vector<int> numbers;
};
