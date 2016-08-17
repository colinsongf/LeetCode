# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        stack = []
        result = None
        i = 0
        size = len(s)
        while i < size:
            if s[i] in '-0123456789':
                number = 0
                f = False
                if s[i] == '-':
                    f = True
                    i += 1
                while i < size and s[i] in '0123456789':
                    number *= 10;
                    number += int(s[i])
                    i += 1
                if f:
                    number = ~number + 1
                if not stack:
                    intlist = NestedInteger()
                    intlist.setInteger(number)
                    result = intlist
                else:
                    top = stack[-1]
                    intlist = NestedInteger()
                    intlist.setInteger(number)
                    top.add(intlist)
            elif s[i] == '[':
                if not stack:
                    intlist = NestedInteger()
                    stack.append(intlist)
                    result = intlist
                else:
                    top = stack[-1]
                    intlist = NestedInteger()
                    stack.append(intlist)
                    top.add(intlist)
                i += 1
            elif s[i] == ']':
                stack.pop()
                i += 1
            elif s[i] == ',':
                i += 1
        return result
        
