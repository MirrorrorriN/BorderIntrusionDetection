def ladder(s1,s2,word):
    wordlist=list(word)
    n=len(wordlist)
    m=len(s1)
    #flag=[-1]*n
    alphabet="abcdefghijklmnopqrstuvwxyz"
    flag=[-1]*n
    queue=[-1]*(n+1)    
    start=0
    end=0
    opt=2
    
    while(end<=n+1):
       
        for i in range(start,end+1):
            temp=0
            if start==0:
                s=s1
            else:
                s=wordlist[queue[i]]
                
            for j in range(m):
                for k in alphabet:
                    st=s[:j]+k+s[j+1:]
                    if (st==s2):
                        return opt
                    elif(st in wordlist)and(flag[wordlist.index(st)]==-1):
                        temp=temp+1        
                        queue[end+temp]=wordlist.index(st)
                        flag[wordlist.index(st)]=1
        if(temp==0):
            return 0
        end=end+temp
        start=end+1-temp
        opt=opt+1
    return 0
        


if __name__=="__main__":
	s1="hot"
	s2="dot"
	wordlist=["hot","dot"]
	opt=ladder(s1,s2,wordlist)
	print opt
