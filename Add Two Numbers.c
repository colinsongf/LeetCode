/**
 * Definition for singly-linked list.
*/
struct ListNode* createListNode(int val) {
    struct ListNode *node = malloc(sizeof(struct ListNode));
    if (!node)
        exit(1);
    node->val = val;
    node->next = NULL;
    return node;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int step = 0;
    int val ;
    struct ListNode *current ,*prev = NULL, *list = NULL, *leave;
    while (l1 && l2) {
        val =l1->val + l2->val + step;
        if (val >= 10) {
            val = val % 10;
            step = 1;
        }else 
            step = 0;
        current = createListNode(val);
        if (!prev)
            list = current;
        else
            prev->next = current;
        prev = current;
        l1 = l1->next;
        l2 = l2->next;
    }
    leave = l1?l1:l2;
    while (leave) {
        val = leave->val + step;
        if (val >= 10) {
            val = val % 10;
            step = 1;
        }else
            step = 0;
        current = createListNode(val);
        if (!prev)
            list = current;
        else
            prev->next = current;
        prev = current;
        leave = leave->next;
    }
    if (step) {
        current = createListNode(1);
        if (!prev)
            list = current;
        else
            prev->next = current;
    }
    return list;
}