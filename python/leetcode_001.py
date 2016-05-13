def twoSum(nums,target):
    ori=[0]*(len(nums))
    for i in range(len(nums)):
        ori[i]=nums[i]
    list.sort(nums)
    start=0
    end=len(nums)-1
    a=-1
    b=-1
    for i in range(len(nums)-1):
        temp=nums[start]+nums[end]
        if temp==target:
            break
        if temp>target:
            end=end-1
        else:
            start=start+1
    for i in range(len(nums)):
        if(ori[i]==nums[start])and(a==-1):
            a=i
            if(a!=-1)and(b!=-1):
                break
        elif(ori[i]==nums[end])and(b==-1):
            b=i
            if(a!=-1)and(b!=-1):
                break
    return [min(a,b),max(a,b)]
        

if __name__=="__main__":
    s=[0,4,3,2,7,0]
    ans=twoSum(s,9)
    print ans
