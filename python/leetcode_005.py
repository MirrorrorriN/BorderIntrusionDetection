def longestPalindrome(s):
    n=len(s)
    ans=""
    maxlen=0
    start=0
    for i in range(n):
        j=i-1
        k=i+1
        cur=1
        while(j>=0)and(k<n)and(s[j]==s[k]):
            j=j-1
            k=k+1
            cur=cur+2
        if (cur>maxlen):
            maxlen=cur
            start=j+1
    for i in range(n-1):
        j=i
        k=i+1
        cur=0
        while(j>=0)and(k<n)and(s[j]==s[k]):
            j=j-1
            k=k+1
            cur=cur+2
        if (cur>maxlen):
            maxlen=cur
            start=j+1
    return s[start:start+maxlen]  
if __name__=="__main__":
    s="aceecabacdks"
    ans=longestPalindrome(s)
    print ans
