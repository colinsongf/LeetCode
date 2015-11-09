class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        super(TreeNode, self).__init__()
        self.val = x
        self.left=self.right=None    

class Solution:
    def rightSideView(self, root):
        queue1,queue2=[],[]
        answer=[]
        if not root:
            return answer
        queue1.append(root)
        while queue1:
            top=queue1.pop(0)
            if top.left:
                queue2.append(top.left)
            if top.right:
                queue2.append(top.right)
            if not queue1:
                answer.append(top.val)
                queue1=queue2
                queue2=[]
        return answer
