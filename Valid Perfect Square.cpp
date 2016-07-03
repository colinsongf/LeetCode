class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 0) return false;
        if (num <= 1) return true;
        int head = 2, rear = num - 1;
        if (rear >= 46340)
            rear = 46340;
        int mid;
        while (head <= rear) {
            mid = (head + rear) >> 1;
            if (mid * mid > num) {
                rear = mid - 1;
            } else if (mid * mid < num) {
                head = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
