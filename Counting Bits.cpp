class Solution {
public:
    void expandanswer(vector<int>& answer) {
        int size = answer.size();
        for (int i = 0;i != size; ++i) {
            answer.push_back(answer[i] + 1);
        }
    }

    vector<int> countBits(int num) {
        vector<int> answer = {0};
        if (!num) {
            return answer;
        }
        answer.push_back(1);
        if (num == 1) {
            return answer;
        }
        while (answer.size() * 2 <= num + 1) {
            expandanswer(answer);
        }
        if (answer.size() < num + 1) {
            int leave = num + 1 - answer.size();
            int i = 0;
            while (leave--) {
                answer.push_back(answer[i++] + 1);
            }
        }
        return answer;
    }
};
