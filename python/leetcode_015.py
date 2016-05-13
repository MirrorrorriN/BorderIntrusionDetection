class Solution(object):
    def threeSum(self, nums):
        result=[]
        nhash={}
        orderlist=[]
        for n in nums:
            if(n not in nhash):
                nhash[n]=1
            elif (nhash[n]==1)or((n==0) and(nhash[0]==2)):
                nhash[n]=nhash[n]+1    
    
        for n,count in nhash.iteritems():
            if (count==2) and (n==0 or (-2*n not in nhash)):
                nhash[n]=1
        for n,count in sorted(nhash.iteritems()):
            for i in range(count):
                orderlist.append(n)
        n=len(orderlist)
        while(n>=4):
            minv=-(orderlist[n-2]+orderlist[n-1])
            maxv=-(orderlist[0]+orderlist[1])
            left=n
            right=-1
            for i in range(n):
                if orderlist[i]>=minv:
                    left=i
                    break
            for i in range(n-1,-1,-1):
                if orderlist[i]<=maxv:
                    right=i
                    break
            if (left==0) and (right==n-1):
                break
            orderlist=orderlist[left:right+1]
            n=len(orderlist)
        
        if (n<3):
            return []
        if (0 in nhash) and (nhash[0]==3):
            result.append([0,0,0])
            
        for i in range(n-2):
            
            n1=orderlist[i]
            if n1>=0:
                return result
            if i>0 and n1==orderlist[i-1]:
                continue
            for j in range(i+1,n-1):
                
                n2=orderlist[j]
                if j>i+1 and (n2==orderlist[j-1]):
                    continue
                n3=-(n1+n2)
                if(n3<n2):
                    break
                if(n3 in nhash):
                    if(n3>n2) or (nhash[n3]>1):
                        result.append([n1,n2,n3])
                        
        return result
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
if __name__=="__main__":
    instance=Solution()
    nums=[-1,0,0,0,1, 2, -1, -4]
    ans=instance.threeSum(nums)
    print ans
    
