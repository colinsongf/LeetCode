/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *reverseList(struct ListNode *head) {
	struct ListNode *prev = NULL ,*current = head, *nextone;
	struct ListNode *newhead = NULL;
	while (current) {
		nextone = current->next;
		current->next = prev;
		prev = current;
		current = nextone;
		if (!nextone)
			newhead = prev;
	}
	return newhead;
}

int getListLength(struct ListNode *head){
	int size = 0;
	while (head) {
		size++ ;
		head = head->next;
	}
	return size;
}

int isPalindrome(struct ListNode *head){
	int size = getListLength(head);
	struct ListNode *mid = head;
	int i = 0;
	while (i++ < size/2)
		mid = mid->next;
	mid = reverseList(mid);
	i = 0;
	while (i++ < size/2){
		if (head->val != mid->val)
			return false;
		head = head->next;
		mid = mid->next;
	}
	return true;
}