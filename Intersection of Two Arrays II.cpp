class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> answer;
        if (nums1.cbegin() != nums1.cend() && nums2.cbegin() != nums2.cend())
        {
            sort(nums1.begin(), nums1.end(), less<int>());
            sort(nums2.begin(), nums2.end(), less<int>());
            auto it1 = nums1.cbegin(), it2 = nums2.cbegin();
            while (it1 != nums1.cend() && it2 != nums2.cend()) {
                if (*it1 == *it2) {
                    answer.push_back(*it1);
                    ++it1;
                    ++it2;
                } else if (*it1 > *it2) {
                    ++it2;
                } else {
                    ++it1;
                }
            }
        }
        return answer;
    }
};
