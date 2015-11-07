class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val = x
        self.left,self.right = None,None

class Solution(object):
    def inorderTraversal_iterator(self, root):
        if not root:
            return
        left=self.inorderTraversal_iterator(root.left)
        for node in left:
            yield node
        yield root.val
        right=self.inorderTraversal_iterator(root.right)
        for node in right:
            yield node
    def inorderTraversal(self, root):
        seq = []
        inorder = self.inorderTraversal_iterator(root)
        for node in inorder:
            seq.append(node)
        return seq

ins=Solution()

root=TreeNode(1)
root.left=TreeNode(2)

print ins.inorderTraversal(root)