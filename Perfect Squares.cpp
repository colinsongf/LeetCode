class Solution {
public:
    int numSquares(int n) {
        int m[n + 1];
        for (int i = 0;i <= n; ++i) {
            m[i] = i;
        }
        for (int i = 2;i <= (int)sqrt((double)n); ++i) {
            m[i * i] = 1;
        }
        for (int i = 2;i <= n; ++i) {
            for (int j = 1;j <= (int)sqrt((double)i); ++j) {
                if (m[i - j * j] + m[j * j] < m[i]) {
                    m[i] = m[i - j * j] + m[j * j];
                }
            }
        }
        return m[n];
    }
};