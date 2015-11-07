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

tree=TreeNode(5)
tree3=TreeNode(3)
tree8=TreeNode(8)
tree.left,tree.right=tree3,tree8
tree3.left,tree3.right=TreeNode(1),TreeNode(4)
tree8.left,tree8.right=TreeNode(7),TreeNode(10)

i,v=BSTIterator(tree),[]

while i.hasNext():
    v.append(i.next())
print v