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
	int getListLength(ListNode *head) {
		int length = 0;
		while (head) {
			length += 1;
			head = head->next;
		}
		return length;
	}
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		ListNode* prev = NULL, *current = head;
		if (!head)
			return head;
		int length = getListLength(head);
		int step = length - n;
		int i = 0;
		while (i++ < step) {
			prev = current;
			current = current->next;
		}
		if (!prev)
			return head->next;
		prev->next = current->next;
		return head;
	}
};