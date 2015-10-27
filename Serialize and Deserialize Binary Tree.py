class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:
    def serialize(self, root):
        serializedData = []
        current = root
        stack = []
        while current or stack:
            while current:
                serializedData.append(str(current.val))
                stack.append(current)
                current = current.left
            serializedData.append('#')
            current = stack.pop()
            current = current.right
        serializedData.append('#')
        return ' '.join(serializedData)
    def Deserialize(self, array, sp):
        if array[sp] == '#':
            return None, sp + 1
        root = TreeNode(array[sp])
        sp += 1
        root.left, sp = self.Deserialize(array, sp)
        root.right, sp = self.Deserialize(array, sp)
        return root, sp
    def deserialize(self, data):
        array = data.split(' ')
        sp = 0
        root, sp = self.Deserialize(array, sp)
        return root
