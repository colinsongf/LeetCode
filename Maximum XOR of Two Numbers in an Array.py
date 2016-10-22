#Define Trie Start
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
    def insert(self, ch):
        if ch == '0':
            if not self.left:
                self.left = TrieNode()
            return self.left
        else:
            if not self.right:
                self.right = TrieNode()
            return self.right
    def getXOR(self, step, newval):
        if step == 31:
            return ''
        if not self.left and not self.right:
            return '0'
        if newval[step] == '0':
            if self.right:
                return '1' + self.right.getXOR(step + 1, newval)
            else:
                return '0' + self.left.getXOR(step + 1, newval)
        else:
            if self.left:
                return '1' + self.left.getXOR(step + 1, newval)
            else:
                return '0' + self.right.getXOR(step + 1, newval)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertNode(self, newval):
        current = self.root
        for ch in newval:
            current = current.insert(ch)
    def getXOR(self, newval):
        bit_xor = self.root.getXOR(0, newval)
        return bit_xor

#Define Trie End

def num2Bit(number):
    bit = ''
    while number:
        bit = str(number % 2) + bit
        number /= 2
    return '0' * (31 - len(bit)) + bit

def bit2Num(bit):
    num = 0
    for i, ch in enumerate(bit[::-1]):
        if ch == '1':
            num += (2 ** i)
    return num

class Solution:
    def findMaximumXOR(self, nums):
        bitarray = [num2Bit(num) for num in nums]
        trie = Trie()
        for bit in bitarray:
            trie.insertNode(bit)
        max_xor = 0
        for bit in bitarray:
            my_bit_xor = trie.getXOR(bit)
            my_xor = bit2Num(my_bit_xor)
            print my_xor
            if my_xor > max_xor:
                max_xor = my_xor
        return max_xor
#先按照31位二进制为每个数字插入到Trie树，再用每个数的31位二进制在Trie树中按反序搜索，得到每个数的最大XOR
ins = Solution()
print ins.findMaximumXOR([3, 10, 5, 25, 2, 8])
