class Solution:
    # @return an integer
    def reverse(self, x):
        number=x if x>=0 else (-1)*x
        reversenum=0
        while number:
            reversenum*=10
            reversenum+=number%10
            number/=10
        if reversenum>2147483647 or reversenum<-2147483648:
            reversenum=0
        return reversenum if x>=0 else reversenum*(-1)