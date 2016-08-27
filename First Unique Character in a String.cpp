class Solution {
public:
    int firstUniqChar(string s) {
        string::iterator it;
        map<char, int> counter;
        map<char, int>::iterator mit;
        for (it = s.begin();it != s.end(); ++it)
        {
            mit = counter.find(*it);
            if (mit == counter.end())
            {
                counter[*it] = 1;
            }
            else
            {
                counter[*it] += 1;
            }
        }
        for (it = s.begin();it != s.end(); ++it)
        {
            mit = counter.find(*it);
            if (mit->second == 1)
            {
                return it - s.begin();
            }
        }
        return -1;
    }
};
