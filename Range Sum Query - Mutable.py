class SegmentTreeNode:
    def __init__(self, start, end, subsum):
        self.__start = start
        self.__end = end
        self.__subsum = subsum
        self.left = self.right = None
    def showme(self):
        print '[%d, %d] = %d' % (self.__start, self.__end, self.__subsum)
    def updateSubsum(self, add):
        self.__subsum += add
    @property
    def split(self):
        return (self.__start + self.__end) / 2
    @property
    def subsum(self):
        return self.__subsum
    @property
    def start(self):
        return self.__start
    @property
    def end(self):
        return self.__end

def createSegmentTree(head, rear):
    tree = SegmentTreeNode(head, rear, getsubsum(head, rear))
    if head < rear:
        split = tree.split
        tree.left, tree.right = createSegmentTree(head, split), createSegmentTree(split + 1, rear)
    return tree

def searchsubsum(start, end, root):
    #we assume that start != end
    if start > end:return 0
    if start == root.start and end == root.end:return root.subsum
    split = root.split
    if split < start:return searchsubsum(start, end, root.right)
    elif split > end:return searchsubsum(start, end, root.left)
    else:return searchsubsum(start, split, root.left) + searchsubsum(split + 1, end, root.right)
    #start <= split <= end

def updateSegmentTree(pos, diff, root):
    if root:
        root.updateSubsum(diff)
        updateSegmentTree(pos, diff, root.left) if root.split >= pos else updateSegmentTree(pos, diff, root.right)

class NumArray(object):
    def __init__(self, nums):
        self.array = nums
        if not self.array:return
        size = len(nums)
        subsumheadby = [0 for i in nums]
        subsumheadby[-1] = nums[-1]
        for i in range(size - 2, -1, -1):
            subsumheadby[i] = subsumheadby[i + 1] + nums[i]
        def getsubsum(start, end):
            if end >= size - 1:
                return subsumheadby[start]
            return subsumheadby[start] - subsumheadby[end + 1]

        def createSegmentTree(head, rear):
            tree = SegmentTreeNode(head, rear, getsubsum(head, rear))
            if head < rear:
                split = tree.split
                tree.left = createSegmentTree(head, split)
                tree.right = createSegmentTree(split + 1, rear)
            return tree
        self.root = createSegmentTree(0, size - 1)
    def update(self, i, val):
        if not self.array:return
        updateSegmentTree(i, val - self.array[i], self.root)
        self.array[i] = val
    def sumRange(self, i, j):
        if not self.array:return 0
        return self.array[i] if i == j else searchsubsum(i, j, self.root)
