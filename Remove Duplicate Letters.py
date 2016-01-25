class Solution(object):
    def ifOk(self, someMap, minPos):
        for key in someMap:
            if someMap[key][-1] < minPos:
                return False
        return True
    def getKey(self, someMap):
        targetkey = None
        minPos = -1
        for key in sorted(someMap.keys()):
            minPos = someMap[key][0]
            if self.ifOk(someMap, minPos):
                targetkey = key
                break
        del someMap[targetkey]
        otherkeys = someMap.keys()
        for otherkey in otherkeys:
            while someMap[otherkey] and someMap[otherkey][0] < minPos:
                someMap[otherkey].pop(0)
            if not someMap[otherkey]:
                del someMap[otherkey]
        return targetkey

    def removeDuplicateLetters(self, s):
        dataMap = {}
        for i, ch in enumerate(s):
            dataMap[ch] = dataMap.get(ch, [])
            dataMap[ch].append(i)
        answer = ''
        while dataMap:
            answer += self.getKey(dataMap)
        return answer
