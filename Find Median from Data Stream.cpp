class MedianFinder {
public:
    // Adds a number into the data structure.
    void addNum(int num) {
        maxHeap.push(num);
        if (maxHeap.size() == 1) {
            return ;
        }
        if (maxHeap.size() > minHeap.size() + 1) {
            int movesth = maxHeap.top();
            maxHeap.pop();
            minHeap.push(movesth);
        } else if (maxHeap.top() > minHeap.top()) {
            int movesth = maxHeap.top();
            maxHeap.pop();
            minHeap.push(movesth);
            movesth = minHeap.top();
            minHeap.pop();
            maxHeap.push(movesth);
        }
    }

    // Returns the median of current data stream
    double findMedian() {
        return minHeap.size() == maxHeap.size() ? (minHeap.top() + maxHeap.top()) / 2.0 : maxHeap.top();
    }
private:
    priority_queue<int, vector<int>, greater<int> > minHeap;
    priority_queue<int> maxHeap;
};