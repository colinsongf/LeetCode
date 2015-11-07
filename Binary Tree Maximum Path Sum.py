class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self,x):
        super(TreeNode, self).__init__()
        self.val = x
        self.left=self.right=None        

class Solution:
    def __init__(self):
        self.maxpath=-2**31
    def _maxPathSum(self, root):
        if not root:
            return 0
        #three path:left=>root,right=>root,left=>root=>right
        leftpath,rightpath=self._maxPathSum(root.left),self._maxPathSum(root.right)
        maxValue=max(root.val+leftpath,root.val+rightpath,root.val+leftpath+rightpath,root.val)
        if maxValue>self.maxpath:
            self.maxpath=maxValue
        retValue=max(root.val,root.val+leftpath,root.val+rightpath)
        return retValue
    def maxPathSum(self, root):
        self._maxPathSum(root)
        return self.maxpath

root=TreeNode(1)
root.left,root.right=TreeNode(2),TreeNode(3)

ins=Solution()
print ins.maxPathSum(root)