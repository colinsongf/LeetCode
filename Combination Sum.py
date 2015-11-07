class Answer(object):
    """docstring for ClassName"""
    def __init__(self, vertex ,parent, summary):
        self.parent=parent
        self.vertex=vertex
        self.summary=summary

def getPath(ansroot):
    path=[]
    while ansroot.vertex!=-1:
        path.append(ansroot.vertex)
        ansroot=ansroot.parent
    return path[::-1]

class Solution:
    def combinationSum(self, candidates,target):
        root=Answer(-1,None,0)
        stack=[]
        stack.append(root)
        candidates.sort()
        answerList=[]
        while stack:
            top=stack.pop()
            if top.summary>target:
                continue
            elif top.summary==target:
                ianswer=getPath(top)
                answerList.append(ianswer)
                continue
            for candidate in candidates:
                if candidate < top.vertex:
                    continue
                if top.summary+candidate>target:
                    break
                nextroot=Answer(candidate,top,top.summary+candidate)
                stack.append(nextroot)
        return answerList

ins=Solution()
print ins.combinationSum([2,3,6,7],7)