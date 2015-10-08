class MaxStack {
public:
    void push(int x) {	
    	mystack.push(x);
		if (maxstack.empty() || x >= maxstack.top())
			maxstack.push(x);
	}
    void pop() {
        int top = mystack.top();
		if (top == maxstack.top())
			maxstack.pop();
		mystack.pop();
    }
    int top() {
        return mystack.top();
    }
    int getMax() {
        return maxstack.top();
    }
    int empty() {
        return mystack.empty();
    }
private:
	stack<int> mystack;
	stack<int> maxstack;
};

class Queue{
public:
    void enqueue(int val){
        instack.push(val);
    }
    int dequeue(){
        if (outstack.empty()) 
            while (!instack.empty()) {
                outstack.push(instack.top());
                instack.pop();
            }
        int top = outstack.top();
        outstack.pop();
        return top;
    }
    int getMax(){
        if (!instack.empty() && !outstack.empty()) 
            return instack.getMax() > outstack.getMax() ? instack.getMax() : outstack.getMax();
        if (!instack.empty()) 
            return instack.getMax();
        if (!outstack.empty()) 
            return outstack.getMax();
        return -1;
    }
private:
    MaxStack instack;
    MaxStack outstack;
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> answer;
        if (!k)
            return answer;
         Queue myque;
    int i;
    for (i = 0;i < k; ++i) 
        myque.enqueue(nums[i]);
    answer.push_back(myque.getMax());
     for (i = k;i < nums.size(); ++i) {
        myque.dequeue();
        myque.enqueue(nums[i]);
        answer.push_back(myque.getMax());
     }
     return answer;
    }
};