class Solution:
    def makeanswer(self,answer,words,L):
        stringanswer=[]
        for pos in answer[:-1]:
            start,end,subsum=pos
            subsum-=(end-start)
            spaces=L-subsum
            string=''
            if start==end:
                string=words[start]+(' '*spaces)
                stringanswer.append(string)
                continue
            spacesSize=[spaces/(end-start) for x in range(end-start)]
            spaceSp=0
            fuyu=spaces%(end-start)
            while fuyu:
                spacesSize[spaceSp]+=1
                fuyu-=1
                spaceSp+=1
            string=words[start]+(' '*spacesSize[0])
            i=start+1
            while i<end:
                string=string+words[i]+(' '*spacesSize[i-start])
                i+=1
            string+=words[end]
            stringanswer.append(string)
        
        start,end,subsum=answer[-1]
        string=words[start]
        i=start+1
        while i<=end:
            string=string+' '+words[i]
            i+=1
        while len(string)!=L:
            string=string+' '
        stringanswer.append(string)
        return stringanswer
    def fullJustify(self, words, L):
        wordlen=[len(word) for word in words]
        size=len(words)
        i=0
        answer=[]
        while i<size:
            subsum=wordlen[i]
            j=i+1
            while j<size and subsum+wordlen[j]+1<=L:
                subsum+=wordlen[j]+1
                j+=1
            end=j-1
            answer.append((i,end,subsum))
            i=j
        return self.makeanswer(answer,words,L) 
