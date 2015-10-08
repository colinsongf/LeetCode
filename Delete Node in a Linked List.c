/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    if (!node)
        return ;
    struct ListNode *target = node->next;
    node->val = target->val;
    node->next = target->next;
    free(target);
    //Saying that except the tail in this problem
}