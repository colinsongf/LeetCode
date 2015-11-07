class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=self.right=self.next=None

class Solution:
    def addList(self,head,new):
        if not head:
            return new
        head.next=self.addList(head.next,new)
        return head
    def connect(self,root):
        if not root:
            return
        queue1,queue2=[],[]
        layerlist1=root
        layerlist2prev=None
        layerlist2=None
        while layerlist1:
            top=layerlist1
            layerlist1=layerlist1.next
            if top.left:
                if not layerlist2:
                    layerlist2prev=layerlist2=top.left
                else:
                    layerlist2prev.next=top.left
                    layerlist2prev=layerlist2prev.next
            if top.right:
                if not layerlist2:
                    layerlist2prev=layerlist2=top.right
                else:
                    layerlist2prev.next=top.right
                    layerlist2prev=layerlist2prev.next
            if not layerlist1:
                layerlist1=layerlist2
                layerlist2=None

def debug(node):
    if not node:
        print
        return
    print node.val
    debug(node.next)

root=TreeNode(0)
root1=TreeNode(1)
root1.left=root3=TreeNode(3)
root1.right=TreeNode(4)
root2=TreeNode(2)
root2.left=TreeNode(5)
root2.right=TreeNode(6)
root.left=root1
root.right=root2

ins=Solution()
ins.connect(root)

debug(root3)