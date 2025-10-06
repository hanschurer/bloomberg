class Solution:
    def reverse(self, x: int) -> int:
        reverse=''
        num=abs(x)
        if x==0:
            return 0
        while num>0:
            reverse+=str(num%10)
            num=num//10
        reverse = int(reverse)
        if x<0:
            reverse=reverse * -1
        if abs(reverse) > 2147483647:
            return 0
        return reverse




#x =123  output:321
