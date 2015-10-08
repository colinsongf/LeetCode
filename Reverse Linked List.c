/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
if(!head)
		return NULL;
	struct ListNode *nextone=head->next;
	if(!nextone)
		return head;
	head->next=NULL;
	struct ListNode *newhead=reverseList(nextone);
	nextone->next=head;
	return newhead;
}