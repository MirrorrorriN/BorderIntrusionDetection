##class Solution(object):
##    def hammingWeight(self,n):
##        hw=0
##        if (n>2**32-1):
##            return hw
##        while(n>0):
##            hw=hw+n%2
##            n=n/2
##        return hw
class Solution(object):
    def hammingWeight(self,n):
        hw=0
        if (n>2**32-1):
            return hw
        while(n>0):
            t1=n>>1   #Attention
            t2=t1<<1
            if(n!=t2):
                hw=hw+1
            n=t1
        return hw
if __name__=="__main__":
    n=2**32
    x=Solution()
    ans=x.hammingWeight(n)
    print ans
