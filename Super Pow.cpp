int powerMod(int a, int x) {
    //assume x <= 10
    int i, answer = 1;
    for (i = 0;i < x; ++i) {
        answer *= (a % 1337);
        answer %= 1337;
    }
    return answer;
}

class Solution {
public:
    int superPow(int a, vector<int> &b) {
        map<int, int> resultFor1to10mi;
        int answer = 1;
        resultFor1to10mi[1] = powerMod(a, 10);
        for (int i = 2;i < b.size(); ++i) {
            int t = resultFor1to10mi[i - 1];
            int subanswer = 1;
            for (int j = 0;j < 10; ++j) {
                subanswer *= t;
                subanswer %= 1337;
            }
            resultFor1to10mi[i] = subanswer;
        }
        for (int i = b.size() - 1;i >= 0; --i) {
            int t;
            if (i == b.size() - 1) {
                t = powerMod(a, b[i]);
            } else {
                t = resultFor1to10mi[b.size() - 1 - i];
                t = powerMod(t, b[i]);
            }
            answer *= t;
            answer %= 1337;
        }
        return answer;
    }
};
