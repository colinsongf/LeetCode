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

ins=Solution()
tree=ins.buildTree([1,4,5,6,7,8,9,10],[1,6,5,4,9,8,10,7])

preOrder(tree)