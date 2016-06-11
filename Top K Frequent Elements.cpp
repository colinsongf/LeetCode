struct Comp {
    bool operator() (const pair<int, int>& p1, const pair<int, int>& p2) {
        return p1.second < p2.second;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counter;
        for (int num: nums) {
            if (counter.find(num) == counter.end()) {
                counter[num] = 1;
            } else {
                counter[num] += 1;
            }
        }
        vector<pair<int, int> > vec;
        for (auto it = counter.begin();it != counter.end(); ++it) {
            vec.push_back(*it);
        }
        make_heap(vec.begin(), vec.end(), Comp());
        vector<int> answer;
        for (int i = 0;i < k; ++i) {
            pair<int, int> top = vec.front();
            answer.push_back(top.first);
            pop_heap(vec.begin(), vec.end(), Comp());vec.pop_back();
        }
        return answer;
    }
};
