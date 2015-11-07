class Solution(object):
    def preorder(self, root):
        if not root:
            return
        yield root.val
        left = self.preorder(root.left)
        for l in left:
            yield l
        right = self.preorder(root.right)
        for r in right:
            yield r
    def preorderTraversal(self, root):
        preorder=[]
        pre = self.preorder(root)
        for node in pre:
            preorder.append(node)
        return preorder
ins=Solution()
print ins.preorderTraversal(None)        