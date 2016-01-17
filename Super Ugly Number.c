int nthSuperUglyNumber(int n, int* primes, int primesSize) {
    if (n == 1) {
        return 1;
    }
    int i, j = 1, k, min, sel;
    int uglyArray[n];
    int *currentPoint[primesSize];
    uglyArray[0] = 1;
    for (i = 0;i < primesSize; ++i) {
        currentPoint[i] = uglyArray;
    }
    while (j <= n - 1) {
        min = *currentPoint[0] * primes[0];
        sel = 0;
        for (k = 1;k < primesSize; ++k) {
            if (*currentPoint[k] * primes[k] < min) {
                min = *currentPoint[k] * primes[k];
                sel = k;
            }
        }
        for (k = 0;k < primesSize; ++k) {
            while (*currentPoint[k] * primes[k] == min) {
                ++currentPoint[k];
            }
        }
        uglyArray[j++] = min;
    }
    return uglyArray[n - 1];
}
