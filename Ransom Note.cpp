class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> mapper;
        map<char, int>::iterator it;
        for (int i = 0;i < magazine.size(); ++i) {
            it = mapper.find(magazine[i]);
            if (it == mapper.end())
            {
                mapper[magazine[i]] = 1;
            }
            else
            {
                mapper[magazine[i]] += 1;
            }
        }
        for (int i = 0;i < ransomNote.size(); ++i)
        {
            it = mapper.find(ransomNote[i]);
            if (it == mapper.end())
            {
                return false;
            }
            else
            {
                if (mapper[ransomNote[i]] == 0)
                {
                    return false;
                }
                mapper[ransomNote[i]] -= 1;
            }
        }
        return true;
    }
};
