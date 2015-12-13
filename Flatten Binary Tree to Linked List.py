class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val=x
        self.left=self.right=None

class Solution:
    def arrage(self,root):
        rear=root
        origin_right=root.right
        if root.left:
            root.right,rear=self.arrage(root.left)
            root.left=None
        if origin_right:
            rear.right,rear=self.arrage(origin_right)
        return root,rear

    def flatten(self,root):
        if not root:
            return root
        self.arrage(root)
