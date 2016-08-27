class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0, j = numbers.size() - 1;
        vector<int> answer;
        while (i < j)
        {
            if (numbers[i] + numbers[j] == target)
            {
                answer.push_back(i + 1);
                answer.push_back(j + 1);
                break;
            }
            else if (numbers[i] + numbers[j] < target)
            {
                ++i;
            }
            else
            {
                --j;
            }
        }
        return answer;
    }
};
