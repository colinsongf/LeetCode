#include <stdio.h>
#include <stdlib.h>

struct ListNode *deleteDuplicates(struct ListNode *head){
	if(!head)
		return head;
	struct ListNode *prev=head,*cur=head->next,*nextone;
	while(cur){
		nextone=cur->next;
		if(cur->val==prev->val){
			prev->next=NULL;
		}else{
			prev->next=cur;
			prev=cur;
		}
		cur=nextone;
	}
	return head;
}
