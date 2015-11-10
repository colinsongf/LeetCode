class NumArray {
public:
    NumArray(vector<int> &nums) : subSummary(nums.size()) {
        if (nums.size() == 0) {
            available = false;
        } else {
            available = true;
            subSummary[0] = nums[0];
            for (int i = 1;i < nums.size(); ++i) {
                subSummary[i] = subSummary[i - 1] + nums[i];
            }
        }
    }

    int sumRange(int i, int j) {
        if (available)
            return i > 0 ? subSummary[j] - subSummary[i - 1] : subSummary[j];
        else
            return 0;
    }
private:
    vector<int> subSummary;
    bool available;
};