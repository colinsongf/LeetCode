class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        prev,current = head,head.next
        while current:
            nextone = current.next
            if prev.val<=current.val:
                prev = current
                current = current.next
                continue
            if head.val >=current.val:
                prev.next=current.next
                current.next=head
                head=current
                current=nextone
                continue
            scan = head
            scanprev = None
            while scan.val <= current.val and scan != current:
                scanprev = scan
                scan = scan.next
            if scan != current:
                prev.next=current.next
                if scanprev:
                    current.next=scan
                    scanprev.next=current
                else:
                    current.next=head
                    head=current
            else:
                prev = current
            current = nextone
        return head