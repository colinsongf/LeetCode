class Item:
    def __init__(self, vertex):
        self.__vertex = vertex
        self.__status = 0
    def addStatus(self):
        self.__status += 1
    @property
    def finished(self):
        return self.__status == 2
    @property
    def vertex(self):
        return self.__vertex

class Solution(object):
    def isValidSerialization(self, preorder):
        if not preorder:return False
        array = preorder.split(',')
        if len(array) == 1 and array[0] == '#':return True
        stack = []
        node_array = [Item(i) for i in array]
        stack.append(node_array[0])
        for node in node_array[1:]:
            if not stack:return False
            stack[-1].addStatus()
            if stack[-1].finished:stack.pop()
            if node.vertex != '#':stack.append(node)
        return stack == []