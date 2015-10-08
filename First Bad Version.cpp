// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int i = 0, j = n, mid;
        while (i < j) {
            mid = (j - i) / 2 + i;
            if (isBadVersion(mid + 1)) {
                if (mid ==0 || !isBadVersion(mid)) {
                    return mid + 1;
                } else {
                    j = mid;
                }
            } else {
                i = mid + 1;
            }
        }
        return -1;
    }
};