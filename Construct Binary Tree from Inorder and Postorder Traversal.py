class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=self.right=None

def preOrder(root):
    if not root:
        return
    print root.val
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print root.val
    inOrder(root.right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print root.val

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

ins=Solution()
tree=ins.buildTree([7,4,1,5,6,10,8,9],[1,4,5,6,7,8,9,10])

postOrder(tree)