# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        serializeArray = []
        def prefix(root):
            if not root:
                serializeArray.append('#')
                return
            serializeArray.append(str(root.val))
            prefix(root.left)
            prefix(root.right)
        prefix(root)
        return ' '.join(serializeArray)

    def deserialize(self, data):
        serializeArray = data.split(' ')
        if serializeArray[0] == '#':
            return None
        root = TreeNode(serializeArray[0])
        stack = [root]
        finished = [0]
        for ch in serializeArray[1:]:
            current = stack[-1]
            status = finished[-1]
            if ch != '#':
                newnode = TreeNode(ch)
                if status == 0:
                    current.left = newnode
                    finished[-1] = 1
                elif status == 1:
                    current.right = newnode
                    stack.pop()
                    finished.pop()
                stack.append(newnode)
                finished.append(0)
            else:
                if status == 0:
                    current.left = None
                    finished[-1] = 1
                elif status == 1:
                    current.right = None
                    stack.pop()
                    finished.pop()
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
