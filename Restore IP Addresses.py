class Solution:
    # @param s, a string
    # @return a list of strings
    def __init__(self):
        self.selections=[]
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        self.selections.append((a,b,c,d))
    def availableIP(self,ip):
        for iip in ip:
            if len(iip)>1 and iip[0]=='0':
                return False
            num=int(iip)
            if num>=256:
                return False
        return True
    def restoreIpAddresses(self,string):
        answers=[]
        size=len(string)
        if size<4:
            return answers
        for select in self.selections:
            if sum(select)!=size:
                continue
            mayanswer=[]
            mayanswer.append(string[:select[0]])
            mayanswer.append(string[select[0]:select[0]+select[1]])
            mayanswer.append(string[select[0]+select[1]:select[0]+select[1]+select[2]])
            mayanswer.append(string[select[0]+select[1]+select[2]:select[0]+select[1]+select[2]+select[3]])
            if self.availableIP(mayanswer):
                answers.append('.'.join(mayanswer))
        return answers