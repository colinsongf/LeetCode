class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=self.right=None

class Solution(object):
    def buildTreeMethod(self,inOrder,inhead,inrear,postOrder,pohead,porear):
        if inhead>=inrear:
            return None
        root=TreeNode(postOrder[porear-1])
        position = inOrder.index(postOrder[porear-1])
        subsize = position-inhead
        root.left=self.buildTreeMethod(inOrder,inhead,position,postOrder,pohead,pohead+subsize)
        root.right=self.buildTreeMethod(inOrder,position+1,inrear,postOrder,pohead+subsize,porear-1)
        return root
    def buildTree(self,inOrder,postOrder):
        size=len(inOrder)
        root=self.buildTreeMethod(inOrder,0,size,postOrder,0,size)
        return root
