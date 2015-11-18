class Solution(object):
    def __init__(self):
        self.flag = False
    def checkOut(self, posarray, string):
        if len(posarray) < 3:
            return False
        currentpos = 0
        array = []
        for pos in posarray:
            substring = string[currentpos : currentpos + pos]
            if substring[0] == '0'and len(substring) > 1:
                return False
            array.append(int(substring))
            currentpos = currentpos + pos
        for i in range(len(array) - 2):
            if array[i] + array[i + 1] != array[i + 2]:
                return False
        return True
    def backtrace(self, currentSeq, step, currentPos, string):
        if self.flag:return
        size = len(string)
        if currentPos == size and step > 2:
            if self.checkOut(currentSeq, string):
                self.flag = True
            return
        if step == 0:
            for choice in range(1, size):
                nextseq = [choice]
                self.backtrace(nextseq, step + 1, choice, string)
        elif step == 1:
            for choice in range(1, size - currentPos + 1):
                nextseq = currentSeq[:]
                nextseq.append(choice)
                self.backtrace(nextseq, step + 1, choice + currentPos, string)
        else:
            for choice in range(currentSeq[step - 1], size - currentPos + 1):
                if choice - currentSeq[step - 1] > 1: break
                nextseq = currentSeq[:]
                nextseq.append(choice)
                self.backtrace(nextseq, step + 1, choice + currentPos, string)
    def isAdditiveNumber(self, num):
        self.flag = False
        self.backtrace(None, 0, 0, num)
        return self.flag