class Solution:
    def getBit(self,substr,table):
        bit=0
        for ch in substr:
            nbit=table[ch]
            if nbit>bit:
                bit=nbit-bit
            else:
                bit+=nbit
        return bit
    def romanToInt(self, string):
        table={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        store=['' for x in range(4)]
        stack=list(string)
        select=-1
        panduan=['IVX','XLC','CMD','M']
        while stack:
            top=stack.pop(0)
            if select!=-1:
                if top not in panduan[select]:
                    select=-1
            if select==-1:
                if top=='I' or top=='V':
                    select=0
                elif top=='X' or top=='L':
                    select=1
                elif top=='C' or top=='D':
                    select=2
                else:
                    select=3
            store[select]=store[select]+top
        number=0
        for substr in store:
            if not substr:
                continue
            number+=self.getBit(substr,table)
        return number
