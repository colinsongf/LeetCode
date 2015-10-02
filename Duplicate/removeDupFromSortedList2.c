struct ListNode *deleteDuplicates(struct ListNode *head){
	if(!head)
		return NULL;
	struct ListNode *fakehead=malloc(sizeof(struct ListNode));
	fakehead->next=head;
	struct ListNode *prev2=fakehead,*prev=head,*cur,*nextone;
	int flag=0;
	cur=head->next;
	prev->next=NULL;
	while(cur){
		nextone=cur->next;
		if(prev->val==cur->val){
			flag=1;
		}else{
			if(flag){
				flag=0;
				prev2->next=cur;
				prev=cur;
			}else{
				prev->next=cur;
				cur->next=NULL;
				prev2=prev;
				prev=prev->next;
			}
		}
		cur=nextone;
	}
	if(flag)
		prev2->next=NULL;
	return fakehead->next;
}
