#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *createList(int *data, int size) {
    struct ListNode* head = malloc(sizeof(struct ListNode));
    head->val = *data;
    head->next = NULL;
    struct ListNode* prev = head;
    int i;
    for (i = 1;i < size; ++i) {
        prev->next = malloc(sizeof(struct ListNode));
        prev->next->val = *(data + i);
        prev->next->next = NULL;
        prev = prev->next;
    }
    return head;
}

void displayList(struct ListNode *current) {
    while (current) {
        printf("%d ", current->val);
        current = current->next;
    }
    printf("\n");
}

struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head || !head->next) {
        return head;
    }
    struct ListNode *otherlist = NULL, *otherprev = NULL;
    struct ListNode *current = head, *next, *nextnext, *subrear = head;
    while (current) {
        //next add to otherlist;
        next = current->next;
        nextnext = next ? next->next : NULL;
        if (!otherlist) {
            otherlist = next;
        } else {
            otherprev->next = next; 
        }
        otherprev = next;
        if (otherprev) {
            otherprev->next = NULL;
        }
        //nextnext add to current
        current->next = nextnext;
        current = nextnext;
    }
    while (subrear->next) {
        subrear = subrear->next;
    }
    subrear->next = otherlist;
    return head;
}

int main() {
    int data[] = {1, 2, 3};
    int size = sizeof data / sizeof *data;
    struct ListNode *list = createList(data, size);
    displayList(list);
    list = oddEvenList(list);
    displayList(list);
}
