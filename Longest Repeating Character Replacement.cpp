bool cmp(const pair<const int, int> &i, const pair<const int, int> &j) {
    return i.second < j.second;
}

class Solution {
public:
    int characterReplacement(string s, int k) {
        if (!s.size())
        {
            return 0;
        }
        int window_left = 0, window_right = 0;
        int max_size = 0;
        map<int, int> counter;
        counter[s[0]] = 1;
        while (window_left < s.size() && window_right < s.size())
        {
            map<int, int>::iterator it = max_element(counter.begin(), counter.end(), cmp);
            if (window_right - window_left + 1 - it->second <= k && window_right < s.size())
            {
                if (window_right - window_left + 1 > max_size)
                {
                    max_size = window_right - window_left + 1;
                }
                window_right += 1;
                if (counter.find(s[window_right]) == counter.end())
                {
                    counter[s[window_right]] = 1;
                }
                else
                {
                    counter[s[window_right]] += 1;
                }
            }
            else
            {
                map<int, int>::iterator it = counter.find(s[window_left]);
                it->second -= 1;
                if (!it->second)
                {
                    counter.erase(it);
                }
                window_left += 1;
            }
        }
        return max_size;
    }
};
