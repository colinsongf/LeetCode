class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, x):
        self.val=x
        self.left=self.right=None

class Solution:
    def createtree(self,nodes):
        size=len(nodes)
        all_trees=[]
        if not size:
            return [None]
        if size==1:
            node=TreeNode(nodes[0])
            return [node]
        for i in range(size):
            leftnodes,rightnodes=self.createtree(nodes[:i]),self.createtree(nodes[i+1:])
            if leftnodes and rightnodes:
                for left in leftnodes:
                    for right in rightnodes:
                        rootnode=TreeNode(nodes[i])
                        rootnode.left,rootnode.right=left,right
                        all_trees.append(rootnode)
            elif leftnodes:
                for left in leftnodes:
                    rootnode=TreeNode(nodes[i])
                    rootnode.left=left
                    all_trees.append(rootnode)
            elif rightnodes:
                for right in rightnodes:
                    rootnode=TreeNode(nodes[i])
                    rootnode.right=right
                    all_trees.append(rootnode)
            else:
                rootnode=TreeNode(nodes[i])
                all_trees.append(rootnode)
        return all_trees

    def generateTrees(self,n):
        nodes=[x+1 for x in range(n)]
        return self.createtree(nodes)
