# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.target=-1
        self.pathes=[]
    def addtochild(self,root,parentvalue,prevpath):
        if not root:
            return
        mypath=prevpath[:]
        mypath.append(root.val)
        if not root.left and not root.right:
            if root.val + parentvalue == self.target:
                self.pathes.append(mypath)
        else:
            self.addtochild(root.left,root.val+parentvalue,mypath)
            self.addtochild(root.right,root.val+parentvalue,mypath)

    def pathSum(self,root,target):
        self.target=target
        self.addtochild(root,0,[])
        return self.pathes
        