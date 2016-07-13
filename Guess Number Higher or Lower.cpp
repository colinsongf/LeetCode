int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int head = 1, rear = n, mid;
        while (head <= rear) {
            mid = (head >> 1) + (rear >> 1);
            if (head % 2 == 1 && rear % 2 == 1) {
                mid += 1;
            }
            if (guess(mid) == 1) {
                head = mid + 1;
            } else if (guess(mid) == -1) {
                rear = mid - 1;
            } else {
                return mid;
            }
        }
        return 0;
    }
};
