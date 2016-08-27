class Dentry:
    def __init__(self, level, name):
        self.level = level
        self.name = name
        self.isFile = '.' in name

class Solution(object):
    def lengthLongestPath(self, input):
        lines = input.split('\n')
        stack = [Dentry(1, lines[0])]
        max_size = 0
        for line in lines[1:]:
            current_level = stack[-1].level
            my_level = 1
            while line.startswith('\t'):
                line = line[1:]
                my_level += 1
            if my_level == current_level + 1:
                stack.append(Dentry(my_level, line))
            else:
                if stack[-1].isFile:
                    path = '/'.join([i.name for i in stack])
                    size = len(path)
                    max_size = max(max_size, size)
                while stack and stack[-1].level >= my_level:
                    stack.pop()
                stack.append(Dentry(my_level, line))
        if stack and stack[-1].isFile:
            path = '/'.join([i.name for i in stack])
            size = len(path)
            max_size = max(max_size, size)
        return max_size
