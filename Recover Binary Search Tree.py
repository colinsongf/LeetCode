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

tree=TreeNode(5)
tree7=TreeNode(7)
tree1=TreeNode(1)
tree9=TreeNode(9)
tree.left=tree7
tree.right=tree9
tree7.left=tree1
tree7.right=TreeNode(4)
tree1.right=TreeNode(2)
tree9.left=TreeNode(3)
tree9.right=TreeNode(10)

ins=Solution()
ins.infix_debug(tree)
ins.recoverTree(tree)
print '==='
ins.infix_debug(tree)