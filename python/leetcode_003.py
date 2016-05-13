def lengthOfLongestSubstring(s):
    alphabet=[0]*26
    cur=0
    opt=0
    for i in range(len(s)):
        alphabet[ord(s[i])-ord('a')]=alphabet[ord(s[i])-ord('a')]+1       
    for i in range(len(s)):
        if alphabet[ord(s[i])-ord('a')]==1:
            cur=cur+1
            
        else:
            if(cur>opt): opt=cur
            cur=0
    return opt 
if __name__=="__main__":
    s="kefcnbbef"
    ans=lengthOfLongestSubstring(s)
    print ans  
