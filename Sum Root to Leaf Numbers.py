class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val = x
        self.left=self.right=None

class Solution(object):
    def __init__(self):
        self.sum=0
    def scanTree(self,root,val):
        if not root:
            return
        currentval=val*10+root.val
        if not root.left and not root.right:
            self.sum+=currentval
        if root.left:
            self.scanTree(root.left,currentval)
        if root.right:
            self.scanTree(root.right,currentval)
    def sumNumbers(self, root):
        self.scanTree(root,0)
        return self.sum
