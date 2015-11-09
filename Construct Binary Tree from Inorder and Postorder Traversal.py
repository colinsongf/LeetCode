class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=self.right=None

class Solution(object):
    def buildTreeMethod(self,preorder,phead,prear,inorder,inhead,inrear):
        if inhead>=inrear:
            return None
        root=TreeNode(preorder[phead])
        position = inorder.index(preorder[phead])
        subsize = position-inhead
        root.left=self.buildTreeMethod(preorder,phead+1,phead+1+subsize,inorder,inhead,position)
        root.right=self.buildTreeMethod(preorder,phead+1+subsize,prear,inorder,position+1,inrear)
        return root
    def buildTree(self,preorder,inorder):
        size=len(preorder)
        root=self.buildTreeMethod(preorder,0,size,inorder,0,size)
        return root
