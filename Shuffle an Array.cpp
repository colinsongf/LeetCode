class Solution {
public:
    Solution(vector<int> nums) {
        array = new int[nums.size()];
        size = nums.size();
        copy(nums.begin(), nums.end(), array);
        srand(time(0));
    }
    
    vector<int> reset() {
        vector<int> result(array, array + size);
        return result;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> result(array, array + size);
        vector<int>::iterator it = result.begin();
        unsigned fm = size;
        int pos;
        for (int i = 0;i < size; ++i)
        {
            pos = rand() % (size - i) + i;
            iter_swap(it + i, it + pos);
        }
        return result;
    }
private:
    int *array;
    unsigned size;
};
/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
