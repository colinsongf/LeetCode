class Solution {
public:
vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> answer;
        unordered_map<int, bool> maper;
        for (int i: nums1) {
            maper[i] = false;
        }
        for (int i: nums2) {
            if (maper.find(i) != maper.end()) {
                maper[i] = true;
            }
        }
        for (auto it = maper.begin();it != maper.end(); ++it) {
            if (it->second) {
                answer.push_back(it->first);
            }
        }
        return answer;
    }
};
