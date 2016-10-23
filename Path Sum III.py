# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.counter = 0
    def pathSum(self, root, sum):
        def backtrace(root):
            sub = []
            if not root:
                return sub
            left_sub = backtrace(root.left)
            right_sub = backtrace(root.right)
            sub.append(root.val)
            sub.extend([i + root.val for i in left_sub])
            sub.extend([i + root.val for i in right_sub])
            self.counter += sub.count(sum)
            return sub
        backtrace(root)
        return self.counter
