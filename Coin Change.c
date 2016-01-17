#define CANNOT 1000000

int coinChange(int* coins, int coinsSize, int amount) {
    int m[amount + 1];
    int i, j;
    //init
    m[0] = 0;
    //dynamic
    for (j = 1;j <= amount; ++j) {
        m[j] = CANNOT;
        for (i = 0;i < coinsSize; ++i) {
            if (j >= coins[i] && m[j] > m[j - coins[i]] + 1) {
                m[j] = m[j - coins[i]] + 1;
            }
        }
    }
    return m[amount] == CANNOT ? -1 : m[amount];
}
