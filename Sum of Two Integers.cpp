class Solution {
public:
    int getSum(int a, int b) {
        int xor_result = a, and_result = b, temp;
        while (and_result) {
            temp = xor_result ^ and_result;
            and_result = xor_result & and_result;
            and_result <<= 1;
            xor_result = temp;
        }
        return xor_result;
    }
};
