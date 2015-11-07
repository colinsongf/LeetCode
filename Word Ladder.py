class Answer(object):
    """docstring for Answer"""
    def __init__(self, string,parent,height):
        self.string=string
        self.parent=parent
        self.height=height

def canaccess(word1,word2):
    counter=0
    for ch1,ch2 in zip(word1,word2):
        if ch1!=ch2:
            if counter==1:
                return False
            counter+=1
    return counter==1

class Solution:
    def ladderLength(self,start,end,words):
        ans=(start,1)
        queue=[ans]
        while queue:
            top=queue.pop(0)
            if canaccess(top[0],end):
                return top[1]+1
            it=iter(words)
            for sel in it:
                if canaccess(sel,top[0]):
                    ans=(sel,top[1]+1)
                    queue.append(ans)
                    words.remove(sel)