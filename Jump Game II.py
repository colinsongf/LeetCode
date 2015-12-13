class Solution:
    def jump_low(self, array):
        size=len(array)
        if size<2:
            return 0
        queue1,queue2=[],[]
        queue1.append(0)
        height=0
        visited={}.fromkeys(range(size),0)
        while queue1:
            top=queue1.pop(0)
            #print top,
            if top>=size-1:
                break
            for i in range(1,array[top]+1):
                arrive=top+i
                if arrive>=size or visited[arrive]:
                    continue
                visited[arrive]=1
                queue2.append(top+i)
            if not queue1:
                height+=1
                queue1=queue2[:]
                queue2=[]
        return height
    def jump(self, array):
        size=len(array)
        if size<2:
            return 0
        counter=1
        starting=1
        ending=array[0]
        if ending>=size-1:
            return counter
        while starting<=ending:
            maxvalue=0
            counter+=1
            for i in range(starting,ending+1):
                if i>=size:
                    continue
                if i+array[i]>maxvalue:
                    maxvalue=i+array[i]
            if maxvalue>=size-1:
                return counter
            starting=ending+1
            ending=max(maxvalue,ending)
