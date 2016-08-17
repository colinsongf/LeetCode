/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head): list(head), length(0) {
        ListNode* current = list;
        srand(time(NULL));
        while (current)
        {
            ++length;
            current = current->next;
        }
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        ListNode* current = list;
        unsigned select = rand() % length;
        unsigned i = 0;
        while (i++ < select)
        {
            current = current->next;
        }
        return current->val;
    }
private:
    ListNode* list;
    unsigned length;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
