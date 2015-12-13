class Solution(object):
    def checkRoot(self, root):
        min,max=root.val,root.val
        if root.left:
            l_status,l_min,l_max = self.checkRoot(root.left)
            if root.left.val >= root.val or not l_status or l_min >= root.val or l_max >= root.val:
                return False,min,max
            min=l_min
        if root.right:
            r_status,r_min,r_max = self.checkRoot(root.right)
            if root.right.val <= root.val or not r_status or r_min <= root.val or r_max <= root.val:
                return False,min,max
            max=r_max
        return True,min,max
    def isValidBST(self, root):
        if not root:
            return True
        status,min,max=self.checkRoot(root)
        return status