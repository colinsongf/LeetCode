class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        super(TreeNode, self).__init__()
        self.val = x
        self.left=self.right=None    

class BSTIterator:
    def __init__(self,root):
        self.minstack=[]
        while root:
            self.minstack.append(root)
            root=root.left
    def next(self):
        top=self.minstack.pop()
        if top.right:
            right=top.right
            while right:
                self.minstack.append(right)
                right=right.left
        return top.val
    def hasNext(self):
        return self.minstack
