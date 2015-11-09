class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val=x
        self.left=self.right=None
        
class Solution:
    def __init__(self):
        self.firstNode=self.secondNode=None
        self.wrongNode1=self.wrongNode2=None
    def infix(self,root):
        if not root:
            return
        self.infix(root.left)
        if not self.firstNode:
            self.firstNode=root
        else:
            if self.secondNode:
                self.firstNode=self.secondNode
            self.secondNode=root
            if self.firstNode.val > self.secondNode.val:
                if not self.wrongNode1:
                    self.wrongNode1=self.firstNode
                    self.wrongNode2=self.secondNode
                else:
                    self.wrongNode2=self.secondNode
        self.infix(root.right)
    def recoverTree(self,root):
        self.infix(root)
        if self.wrongNode1 and self.wrongNode2:
            self.wrongNode1.val,self.wrongNode2.val=self.wrongNode2.val,self.wrongNode1.val

    def infix_debug(self,root):
        if not root:
            return
        self.infix_debug(root.left)
        print (root.val)
        self.infix_debug(root.right)
