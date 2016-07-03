int gcd(int x, int y) {
    int t;
    while (y) {
        t = y;
        y = x % y;
        x = t;
    }
    return x;
}

bool canMeasureWater(int x, int y, int z) {
    if (x + y < z) {
        return false;
    }
    if (x == z || y == z || x + y == z) {
        return true;
    }
    return z % gcd(x, y) == 0;
}
