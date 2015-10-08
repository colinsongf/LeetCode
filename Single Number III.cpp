class Solution {
public:
    int FindNumAppearOnce(vector<int> data) {
        int flag = 0;
        if (data.size() == 0)
            return flag;
        vector<int>::iterator it;
        for (it = data.begin();it != data.end(); ++it)
            flag ^= *it;
        return flag;
    }
    vector<int> singleNumber(vector<int>& data) {
        vector<int> answer;
        if (data.size() < 2) {
        	return answer;
        }
        int flag = FindNumAppearOnce(data);
        int i = 0;
        while(!((1 << i) & flag))
            i++;
        flag = 1 << i;
        vector<int> left,right;
        vector<int>::iterator it;
        for (it = data.begin();it != data.end(); ++it)
            if (flag & (*it))
            	left.push_back(*it);	
            else
            	right.push_back(*it);
        answer.push_back(FindNumAppearOnce(left));
        answer.push_back(FindNumAppearOnce(right));
        return answer;
    }
};