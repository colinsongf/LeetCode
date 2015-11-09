class UndirectedGraphNode(object):
    def __init__(self, x):
        super(UndirectedGraphNode, self).__init__()
        self.label = x
        self.neighbors=[]

def dfs(node):
    visited = []
    stack = []
    stack.append(node)
    while stack:
        top = stack.pop()
        if top.label in visited:
            continue
        print top.label,'(',len(top.neighbors),')'
        visited.append(top.label)
        for neibor in top.neighbors:
            if neibor.label not in visited:
                stack.append(neibor)

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        visited = []
        queue = []
        construct = {}
        queue.append(node)
        retnode = None
        while queue:
            top = queue.pop(0)
            if top.label in visited:
                continue
            newnode = UndirectedGraphNode(top.label) if top.label not in construct else construct[top.label]
            construct[top.label]=newnode
            if not retnode:
                retnode = newnode
            for neibor in top.neighbors:
                if neibor.label == top.label:
                    newnode.neighbors.append(newnode)
                    continue
                newneibor= UndirectedGraphNode(neibor.label) if neibor.label not in construct else construct[neibor.label]
                construct[newneibor.label]=newneibor
                newnode.neighbors.append(newneibor)
                if neibor.label not in visited:
                    queue.append(neibor)
            visited.append(newnode.label)
        return retnode
