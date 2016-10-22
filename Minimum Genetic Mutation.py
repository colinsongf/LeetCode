class SearchNode:
    def __init__(self, vertex, parent = None):
        self.vertex = vertex
        self.parent = parent
        self.height = 0 if not parent else (parent.height + 1)

def diff(seq1, seq2):
    diff_arrary = []
    i = 0
    for s1, s2 in zip(seq1, seq2):
        if s1 != s2:
            diff_arrary.append(i)
        i += 1
    return diff_arrary

class Solution(object):
    def minMutation(self, start, end, bank):
        bank = set(bank)
        current = SearchNode(start)
        queue = [current]
        while queue:
            current = queue.pop(0)
            diff_arrary = diff(current.vertex, end)
            if not diff_arrary:
                return current.height
            for pos in diff_arrary:
                next_vertex = current.vertex[:pos] + end[pos] + current.vertex[pos + 1:]
                if next_vertex in bank:
                    next_node = SearchNode(next_vertex, current)
                    queue.append(next_node)
        return -1
