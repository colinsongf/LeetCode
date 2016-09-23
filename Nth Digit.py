class Solution(object):
    def __init__(self):
        self.slots = [0]
        for i in range(1, 11):
            self.slots.append(self.slots[i - 1] + 9 * (10 ** (i - 1)) * i)
    def findNthDigit(self, n):
        if n < 10:
            return n
        bits = 0
        for i, slot in enumerate(self.slots):
            if n <= self.slots[i]:
                bits = i
                break
        leave = n - self.slots[bits - 1]
        prev = leave / bits - 1 + 10 ** (bits - 1)
        add = leave % bits
        next = prev + 1
        if add == 0:
            return int(str(prev)[-1])
        else:
            return int(str(next)[add - 1])
