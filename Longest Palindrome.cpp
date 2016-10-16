class Solution
{
public:
    int longestPalindrome(string s) {
        map<char, int> counter;
        int answer = 0;
        for (string::iterator it = s.begin();it != s.end(); ++it)
        {
            char ch = *it;
            if (counter.find(ch) == counter.end())
            {
                counter[ch] = 1;
            }
            else
            {
                counter[ch] += 1;
            }
        }
        for (map<char, int>::iterator it = counter.begin();it != counter.end(); ++it)
        {
            answer += (it->second / 2) * 2;
            it->second %= 2;
        }
        for (map<char, int>::iterator it = counter.begin();it != counter.end(); ++it)
        {
            if (it->second)
            {
                answer += 1;
                break;
            }
        }
        return answer;
    }
};
