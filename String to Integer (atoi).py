class Solution:
    def beforereturn(self,number):
        if number>2**31-1:
            number=2**31-1
        elif number<-2**31:
            number=-2**31
        return number
    def atoi(self, string):
        string=string.strip()
        if not string:
            return 0
        result=0
        if string[0] not in '+-0123456789':
            return result
        neg=1
        if string[0]=='+' or string[0]=='-':
            if string[0]=='-':
                neg=(-1)
            string=string[1:]
        for c in string:
            if c not in '0123456789':
                return self.beforereturn(neg*result)
            result*=10
            result+=int(c)
        return self.beforereturn(result*neg)
