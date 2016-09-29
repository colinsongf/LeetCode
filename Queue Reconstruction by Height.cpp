bool cmp_by_1(const pair<int, int>& i, const pair<int, int>& j)
{
    return i.first > j.first;
}

bool cmp_by_2(const pair<int, int>& i, const pair<int, int>& j)
{
    return i.second < j.second;
}

class Solution
{
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        vector<pair<int, int> >answer;
        sort(people.begin(), people.end(), cmp_by_2);
        stable_sort(people.begin(), people.end(), cmp_by_1);
        for (vector<pair<int, int> >::iterator it = people.begin();it != people.end(); ++it)
        {
            pair<int, int> p = *it;
            answer.insert(answer.begin() + it->second, p);
        }
        return answer;
    }
};
