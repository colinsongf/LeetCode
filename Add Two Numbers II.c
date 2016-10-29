struct ListNode* reverseList(struct ListNode* head)
{
    struct ListNode *current = head, *next, *prev = NULL;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        if (!next)
        {
            break;
        }
        current = next;
    }
    return prev;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* nl1 = reverseList(l1);
    struct ListNode* nl2 = reverseList(l2);
    struct ListNode* head = NULL;
    struct ListNode* prev = NULL, *current;
    int jw = 0;
    while (nl1 && nl2)
    {
        current = malloc(sizeof(struct ListNode));
        current->val = (nl1->val + nl2->val + jw) % 10;
        jw = (nl1->val + nl2->val + jw) / 10;
        current->next = NULL;
        if (!prev)
        {
            prev = current;
            head = current;
        }
        else
        {
            prev->next = current;
            prev = current;
        }
        nl1 = nl1->next;
        nl2 = nl2->next;
    }
    while (nl1)
    {
        current = malloc(sizeof(struct ListNode));
        current->val = (nl1->val + jw) % 10;
        jw = (nl1->val + jw) / 10;
        current->next = NULL;
        if (!prev)
        {
            prev = current;
            head = current;
        }
        else
        {
            prev->next = current;
            prev = current;
        }
        nl1 = nl1->next;
    }
    while (nl2)
    {
        current = malloc(sizeof(struct ListNode));
        current->val = (nl2->val + jw) % 10;
        jw = (nl2->val + jw) / 10;
        current->next = NULL;
        if (!prev)
        {
            prev = current;
            head = current;
        }
        else
        {
            prev->next = current;
            prev = current;
        }
        nl2 = nl2->next;
    }
    if (jw)
    {
        current = malloc(sizeof(struct ListNode));
        current->val = jw;
        current->next = NULL;
        if (!prev)
        {
            prev = current;
            head = current;
        }
        else
        {
            prev->next = current;
            prev = current;
        }
    }
    return reverseList(head);
}
