class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D)
    {
        map<int, int> mapper;
        map<int, int>::iterator it;
        int answer = 0;
        int size = A.size();
        for (int i = 0;i < size; ++i)
        {
            for (int j = 0;j < size; ++j)
            {
                int sum = A[i] + B[j];
                it = mapper.find(sum);
                if (it == mapper.end())
                {
                    mapper[sum] = 1;
                }
                else
                {
                    mapper[sum] += 1;
                }
            }
        }

        for (int i = 0;i < size; ++i)
        {
            for (int j = 0;j < size; ++j)
            {
                int sum = C[i] + D[j];
                it = mapper.find(sum * (-1));
                if (it != mapper.end())
                {
                    answer += it->second;
                }
            }
        }
        return answer;
    }
};
