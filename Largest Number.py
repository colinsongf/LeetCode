def mycmp(number1,number2):
    n1,n2=number1,number2
    size1,size2=0,0
    while number1:
        size1+=1
        number1/=10
    while number2:
        size2+=1
        number2/=10
    newnumber1=n1*(10**size2)+n2
    newnumber2=n2*(10**size1)+n1
    return cmp(newnumber1,newnumber2)

class Solution:
    def mycmp(self,number1,number2):
        n1,n2=number1,number2
        size1,size2=1,1
        while number1/10:
            size1+=1
            number1/=10
        while number2/10:
            size2+=1
            number2/=10
        newnumber1=n1*(10**size2)+n2
        newnumber2=n2*(10**size1)+n1
        return cmp(newnumber1,newnumber2)
    def largestNumber(self,array):
        array.sort(cmp=self.mycmp,reverse=True)
        ansstr=''.join([str(x) for x in array])
        while len(ansstr)>1 and ansstr[0]=='0':
            ansstr=ansstr[1:]
        return ansstr
