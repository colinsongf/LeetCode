bool cmp(const pair<int, int>& p1, const pair<int, int>& p2) {
    return p1.first < p2.first;
}

class Solution {
public:
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        if (envelopes.empty()) {
            return 0;
        }
        sort(envelopes.begin(), envelopes.end(), cmp);
        vector<int> increaseLength(envelopes.size(), 0);
        increaseLength[0] = 1;
        for (int i = 1;i < increaseLength.size(); ++i) {
            int max = 1;
            for (int j = i - 1;j >= 0; --j) {
                if (max < (increaseLength[j] + 1) && 
                    envelopes[j].first < envelopes[i].first && 
                    envelopes[j].second < envelopes[i].second) {
                    max = increaseLength[j] + 1;
                }
            }
            increaseLength[i] = max;
        }
        int answer = 0;
        for (auto i : increaseLength) {
            if (i > answer) {
                answer = i;
            }
        }
        return answer;
    }
};
