#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        multimap<int, int> positionMap;
        vector<int> answer;
        int i = 0;
        for (auto num: nums) {
            positionMap.insert(make_pair(num, i++));
        }
        sort(nums.begin(), nums.end());
        auto it_head = nums.cbegin(), it_rear = nums.cend() - 1;
        while (it_head < it_rear) {
            int summary = *it_head + *it_rear;
            if (summary == target) {
                if (*it_head != *it_rear) {
                    auto it1 = positionMap.find(*it_head);
                    auto it2 = positionMap.find(*it_rear);
                    answer.push_back(it1->second);
                    answer.push_back(it2->second);
                } else {
                   auto range = positionMap.equal_range(*it_head);
                   auto it1 = range.first;
                   answer.push_back(it1->second);
                   ++it1;
                   answer.push_back(it1->second);
                }
                break;
            } else if (summary > target) {
                --it_rear;
            } else {
                ++it_head;
            }
        }
        sort(answer.begin(), answer.end());
        return answer;
    }
};

int main() {
    Solution ins;
    vector<int> nums = {0, 7, 1, 0};
    vector<int> answer = ins.twoSum(nums, 0);
    for (auto i: answer) {
        cout << i << endl;
    }
}
