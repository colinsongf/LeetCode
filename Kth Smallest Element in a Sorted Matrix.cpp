class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> heap;
        for (int col = 0;col < k && col < matrix[0].size(); ++col)
        {
            heap.push_back(matrix[0][col]);
        }
        make_heap(heap.begin(), heap.end());
        for (int row = 1;row < matrix.size(); ++row)
        {
            for (int col = 0;col < k && col < matrix[row].size(); ++col)
            {
                if (heap.size() < k)
                {
                    heap.push_back(matrix[row][col]);
                    push_heap(heap.begin(), heap.end());
                }
                else if (heap.front() > matrix[row][col])
                {
                    pop_heap(heap.begin(), heap.end());
                    heap.pop_back();
                    heap.push_back(matrix[row][col]);
                    push_heap(heap.begin(), heap.end());
                }
            }
        }
        return heap.front();
    }
};
