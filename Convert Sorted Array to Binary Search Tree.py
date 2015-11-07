class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        super(TreeNode, self).__init__()
        self.val = x
        self.left,self.right=None,None

class Solution:
    def createTreeNode(self,array,head,rear):
        if head>=rear:
            return None
        mid = (head+rear)/2
        root = TreeNode(array[mid])
        root.left=self.createTreeNode(array,head,mid)
        root.right=self.createTreeNode(array,mid+1,rear)
        return root
    def sortedArrayToBST(self, array):
        if not array:
            return None
        size=len(array)
        tree = self.createTreeNode(array,0,size)
        return tree

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print root.val,
    inOrder(root.right)

def prevOrder(root):
    if not root:
        return
    print root.val,
    prevOrder(root.left)
    prevOrder(root.right)

ins=Solution()
tree = ins.sortedArrayToBST([1,2,3,4,5,6])

prevOrder(tree)
print

inOrder(tree)
print