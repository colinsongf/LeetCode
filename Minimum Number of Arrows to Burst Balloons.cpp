bool cmp(const pair<int, int>& i, const pair<int, int>& j)
{
    return i.first < j.first;
}

class Solution {
public:
    int findMinArrowShots(vector<pair<int, int> >& points)
    {
        int arraw_count = 0;
        if (points.size() == 0)
        {
            return arraw_count;
        }
        sort(points.begin(), points.end(), cmp);
        pair<int, int> currentnode = points[0];
        for (vector<pair<int, int> >::iterator it = points.begin() + 1;it != points.end(); ++it)
        {
            if (it->first <= currentnode.second)
            {
                currentnode.first = it->first;
                currentnode.second = it->second < currentnode.second ? it->second: currentnode.second;
            }
            else//no intersection
            {
                arraw_count += 1;
                currentnode = *it;
            }         
        }
        arraw_count += 1;
        return arraw_count;
    }
};
