/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getLengthOfList(struct ListNode *head) {
    if (!head)
        return 0;
    return getLengthOfList(head->next) + 1;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    int size1 = getLengthOfList(headA);
    int size2 = getLengthOfList(headB);
    int i = 0;
    if (size1 > size2) 
        while (i++ < size1 - size2)
            headA = headA->next;
    else if (size1 < size2) 
        while (i++ < size2 - size1)
            headB = headB->next;
    while (headA && headB && headA != headB)
        headA = headA->next,headB = headB->next;
    return headA == headB ? headA : NULL;
}