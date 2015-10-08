struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *list = NULL,*current = NULL;
    if (!list1)
        return list2;
    if (!list2)
        return list1;
    if (list1->val <= list2->val) {
        list = current = list1;
        list1 = list1->next;
    } else {
        list = current = list2;
        list2 = list2->next;
    }
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }
    while (list1) {
        current->next = list1;
        list1 = list1->next;
        current = current->next;
    }
    while (list2) {
        current->next = list2;
        list2 = list2->next;
        current = current->next;
    }
    current->next = NULL;
    return list;
}