int countNumbersWithUniqueDigits(int n) {
    if (!n)
        return 1;
    int *m = malloc(sizeof(int) * n);
    int i, end, j, result = 0;
    m[0] = 10;
    for (i = 1;i < n; ++i) {
        m[i] = 9;
        end = 9 - i + 1;
        for (j = 9;j >= end; --j) {
            m[i] *= j;
        }
    }
    for (i = 0;i < n; ++i) {
        result += m[i];
    }
    return result;
}
