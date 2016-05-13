def lengthOfLongestSubstring(s):
    cmap={}
    start=0
    cur=0
    opt=0
    for i in range(len(s)):
        if (s[i] not in cmap):
            cmap[s[i]]=i
            cur=cur+1
        else:
            if(cur>opt):
                opt=cur
            cur=cur-(cmap[s[i]]-start)
            temp=cmap[s[i]]
            for j in range(start,cmap[s[i]]+1):
                del cmap[s[j]]
            start=temp+1
            cmap[s[i]]=i
            
    if(cur>opt):
        opt=cur
    return opt  
     
if __name__=="__main__":
    s=""
    ans=lengthOfLongestSubstring(s)
    print ans
