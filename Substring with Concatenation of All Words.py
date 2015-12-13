class Solution:
    def condition(self,dict,need):
        for key in dict:
            if dict[key]!=need[key]:
                return False
        return True
    def counter(self,string,i,length,wsize,dict):
        for i in range(i,i+length,wsize):
            substr=string[i:i+wsize]
            if substr in dict:
                dict[substr]+=1
    def findSubstring(self,string,words):
        wsize,size=len(words[0]),len(string)
        need={}
        length=wsize*len(words)
        for word in words:
            if word not in need:
                need[word]=1
            else:
                need[word]+=1
        answer=[]
        i=0
        while i<=size-length:
            dict={}.fromkeys(need.keys(),0)
            self.counter(string,i,length,wsize,dict)
            if self.condition(dict,need):
                answer.append(i)
            i+=1
        return answer
