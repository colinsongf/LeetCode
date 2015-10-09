#define MIN(a, b, c) ((a) < (b) ? ((a) <= (c) ? (a) : (c)) : ((b) <= (c) ? (b) : (c)))

int nthUglyNumber(int n) {
    int uglynumbers[n];
    uglynumbers[0] = 1;
    if (n <= 1) {
        return uglynumbers[0];
    }
    int pos2 = 0, pos3 = 0, pos5 = 0, currentMax = uglynumbers[0];
    int nextu, nextpos = 1;
    while (nextpos < n) {
        nextu = MIN(uglynumbers[pos2] * 2, uglynumbers[pos3] * 3, uglynumbers[pos5] * 5);
        uglynumbers[nextpos++] = currentMax = nextu;
        while (pos2 < n && uglynumbers[pos2] * 2 <= currentMax)
            ++pos2;
        while (pos3 < n && uglynumbers[pos3] * 3 <= currentMax)
            ++pos3;
        while (pos5 < n && uglynumbers[pos5] * 5 <= currentMax)
            ++pos5;
    }
    return uglynumbers[n - 1];
}