class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> counter;
        string::iterator it;
        for (it = s.begin();it != s.end(); ++it)
        {
            if (counter.find(*it) != counter.end())
            {
                counter[*it] = counter[*it] + 1;
            }
            else
            {
                counter[*it] = 1;
            }
        }
        for (it = t.begin();it != t.end(); ++it)
        {
            if (counter.find(*it) == counter.end())
            {
                return *it;
            }
            else
            {
                if (counter[*it] == 0)
                {
                    return *it;
                }
                else
                {
                    counter[*it] = counter[*it] - 1;
                }
            }
        }
        return '\0';
    }
};
